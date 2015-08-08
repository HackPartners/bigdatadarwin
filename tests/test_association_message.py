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
            x = f.read()
            r = pp.CreateFromDocument(x)
            assert(None is r.sR)
            assert(None is not r.uR)
            assert(1 == len(r.uR.association))
            
            s = AssociationMessage(r.uR.association[0], r, x)
            return s

    def test_association_message_category_next(self):
        m = self.get_association_message_from_file("tests/data/association_message__category_next.xml")
        assert(None is not m)

        assert("RDIT" == m.tiploc)
        assert(AssociationCategory.Next == m.category)
        assert(False is m.cancelled)
        assert(False is m.deleted)

        assert(None is not m.main_service)
        assert(None is not m.associated_service)

        assert("201508083459327" == m.main_service.rid)
        assert(datetime.time(13, 40) == m.main_service.working_arrival_time)
        assert(None is m.main_service.working_pass_time)
        assert(None is m.main_service.working_departure_time)
        assert(datetime.time(13, 41) == m.main_service.public_arrival_time)
        assert(None is m.main_service.public_departure_time)

        assert("201508083458157" == m.associated_service.rid)
        assert(None is m.associated_service.working_arrival_time)
        assert(None is m.associated_service.working_pass_time)
        assert(datetime.time(13, 55) == m.associated_service.working_departure_time)
        assert(None is m.associated_service.public_arrival_time)
        assert(datetime.time(13, 55) == m.associated_service.public_departure_time)

    def test_association_message_category_join(self):
        m = self.get_association_message_from_file("tests/data/association_message__category_join.xml")
        assert(None is not m)

        assert("HORSHAM" == m.tiploc)
        assert(AssociationCategory.Join == m.category)
        assert(False is m.cancelled)
        assert(False is m.deleted)

        assert(None is not m.main_service)
        assert(None is not m.associated_service)

        assert("201508083461173" == m.main_service.rid)
        assert(datetime.time(8, 40) == m.main_service.working_arrival_time)
        assert(None is m.main_service.working_pass_time)
        assert(datetime.time(8, 51) == m.main_service.working_departure_time)
        assert(datetime.time(8, 40) == m.main_service.public_arrival_time)
        assert(datetime.time(8, 51) == m.main_service.public_departure_time)

        assert("201508083471752" == m.associated_service.rid)
        assert(datetime.time(8, 47) == m.associated_service.working_arrival_time)
        assert(None is m.associated_service.working_pass_time)
        assert(None is m.associated_service.working_departure_time)
        assert(datetime.time(8, 47) == m.associated_service.public_arrival_time)
        assert(None is m.associated_service.public_departure_time)

    def test_association_message_category_split(self):
        m = self.get_association_message_from_file("tests/data/association_message__category_split.xml")
        assert(None is not m)

        assert("HORSHAM" == m.tiploc)
        assert(AssociationCategory.Split == m.category)
        assert(False is m.cancelled)
        assert(False is m.deleted)

        assert(None is not m.main_service)
        assert(None is not m.associated_service)

        assert("201508083467351" == m.main_service.rid)
        assert(datetime.time(8, 26) == m.main_service.working_arrival_time)
        assert(None is m.main_service.working_pass_time)
        assert(datetime.time(8, 30) == m.main_service.working_departure_time)
        assert(datetime.time(8, 26) == m.main_service.public_arrival_time)
        assert(datetime.time(8, 30) == m.main_service.public_departure_time)

        assert("201508083472034" == m.associated_service.rid)
        assert(None is m.associated_service.working_arrival_time)
        assert(None is m.associated_service.working_pass_time)
        assert(datetime.time(8, 35) ==  m.associated_service.working_departure_time)
        assert(None is m.associated_service.public_arrival_time)
        assert(datetime.time(8, 35) == m.associated_service.public_departure_time)


