import os
import sys
sys.path.append(os.getcwd())

import datetime
import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messages import ScheduleMessage

class TestScheduleMessage:
    
    def get_schedule_message_from_file(self, file_path):
        with open(file_path) as f:
            r = pp.CreateFromDocument(f.read())
            assert(r.sR is None)
            assert(r.uR is not None)
            assert(len(r.uR.schedule) == 1)
            
            s = ScheduleMessage(r.uR.schedule[0])
            return s
         
    def test_schedule_message(self):
        m = self.get_schedule_message_from_file("tests/data/schedule_message.xml")
        assert(m is not None)

        # Check the basic message properties.
        assert(m.uid == "L06990")
        assert(m.rid == "201507202885757")
        assert(m.headcode == "2W40")
        assert(m.schedule_start_date == datetime.date(2015, 7, 20))
        assert(m.toc_code == "TL")
        assert(m.passenger_service == True)
        assert(m.status == "P")
        assert(m.category == "OO")
        assert(m.active == True)
        assert(m.deleted == False)
        assert(m.charter == False)
        assert(m.cancel_reason is None)

        # Check the size of the list properties.
        assert(len(m.origins) == 1)
        assert(len(m.operational_origins) == 0)
        assert(len(m.intermediate_points) == 13)
        assert(len(m.operational_intermediate_points) == 0)
        assert(len(m.passing_points) == 40)
        assert(len(m.destinations) == 1)
        assert(len(m.operational_destinations) == 0)

        #for a in m.raw.orderedContent():
        #    print(a.value)
        #    print(dir(a))

        # Check the child elemnt basic attributes of the list properties.
        i = m.origins[0]
        assert(i.tiploc == "THBDGS")
        assert(i.activity_codes == "TB")
        assert(i.planned_activity_codes is None)
        assert(i.cancelled == False)
        assert(i.false_tiploc is None)
        assert(i.route_delay is None)
        assert(i.public_departure_time == datetime.time(13, 44))
        assert(i.working_departure_time == datetime.time(17, 2))


