import os
import sys
sys.path.append(os.getcwd())

import datetime
import pytest
import pytz

from darwinpush.messages import AssociationMessage
from darwinpush.messages.AssociationMessage import AssociationCategory
import darwinpush.xb.pushport as pp

class TestAssociationMessage:
    
    def get_association_message_from_file(self, file_path):
        with open(file_path) as f:
            r = pp.CreateFromDocument(f.read())
            assert(r.sR is None)
            assert(r.uR is not None)
            assert(len(r.uR.association) == 1)
            
            s = AssociationMessage(r.uR.association[0], r)
            return s

    def test_association_next_message(self):
        m = self.get_association_message_from_file("tests/data/association_message__category_next.xml")
        assert(None is not m)

        assert("KNGX" == m.tiploc)
        assert(AssociationCategory.Next == m.category)
        assert(False is m.cancelled)
        assert(False is m.deleted)

        assert(None is not m.main_service)
        assert(None is not m.associated_service)

        assert("201508043346518" == m.main_service.rid)
        assert(datetime.time(18, 33) == m.main_service.working_arrival_time)
        assert(None is m.main_service.working_pass_time)
        assert(None is m.main_service.working_departure_time)
        assert(datetime.time(18, 33) == m.main_service.public_arrival_time)
        assert(None is m.main_service.public_departure_time)

        assert("201508043346478" == m.associated_service.rid)
        assert(None is m.associated_service.working_arrival_time)
        assert(None is m.associated_service.working_pass_time)
        assert(datetime.time(18, 53) == m.associated_service.working_departure_time)
        assert(None is m.associated_service.public_arrival_time)
        assert(datetime.time(18, 53) == m.associated_service.public_departure_time)


