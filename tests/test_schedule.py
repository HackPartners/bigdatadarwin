import os
import sys
sys.path.append(os.getcwd())

import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messagefactories.xml import ScheduleXMLMessageFactory
import datetime

# set environment variables to the test database
try_envs = ["DARWINPUSH_DBUSER", "DARWINPUSH_DBPASS", "DARWINPUSH_DBNAME"]

for k in try_envs:
    r = os.getenv("TEST_" + k, None)
    if r is not None:
        os.environ[k] = r

from ex import MyListener, db
from models import Schedule, CallingPoint

def setup_module():
    print("Resetting database")

    db.create_tables([Schedule, CallingPoint], safe=True)

def teardown_module():
    """ Remove the tables so the db is always ready for tests. """
    print("Removing all tables")
    db.drop_tables([Schedule, CallingPoint])

class TestSchedule:

    def from_file(self, file_path):
        """Get schedule message from file."""
        with open(file_path) as f:
            x = f.read()
            r = pp.CreateFromDocument(x)
            assert(None is r.sR)
            assert(None is not r.uR)
            assert(1 == len(r.uR.schedule))

            s = ScheduleXMLMessageFactory.build(r.uR.schedule[0], r, x)
            return s

    def test_duplicate_update(self):
        """Test whether duplicates are actually updated or re-inserted."""

        initial = self.from_file("tests/data/schedule_initial.xml")
        duplicate = self.from_file("tests/data/schedule_duplicate.xml")

        # just to be sure
        assert(initial.uid == duplicate.uid)
        assert(initial.rid == duplicate.rid)

        # force messages directly to listener
        listener = MyListener(None, None)

        listener.on_schedule_message(initial)

        res = Schedule.select().where(
            (Schedule.uid==initial.uid) & (Schedule.rid==initial.rid)
        )

        assert(res.count() == 1)
        s = res[0]
        assert(s.uid == initial.uid)
        assert(s.rid == initial.rid)
        assert(s.toc_code == initial.toc_code)

        cps = CallingPoint.select().where(
            CallingPoint.schedule==s
        ).order_by(CallingPoint.id.asc())

        assert(cps.count() == 2)
        destination_cp = cps[1]
        assert(destination_cp.public_arrival == datetime.time(
            hour=10,
            minute=14))

        listener.on_schedule_message(duplicate)

        res = Schedule.select().where(
            (Schedule.uid==initial.uid) & (Schedule.rid==initial.rid)
        )

        assert(res.count() == 1)
        s_after = res[0]
        assert(s_after.uid == initial.uid) # same uid
        assert(s_after.rid == initial.rid) # same rid
        assert(s_after.toc_code == duplicate.toc_code) # different toc

        # get calling points
        cps = CallingPoint.select().where(
            CallingPoint.schedule == s_after
        ).order_by(CallingPoint.id.asc())

        assert(cps.count() == 2) # should be only two
        destination_cp = cps[1]
        assert(destination_cp.public_arrival == datetime.time(
            hour=10,
            minute=17)) # updated time
