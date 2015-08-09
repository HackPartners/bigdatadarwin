import os
import sys
sys.path.append(os.getcwd())

import datetime
import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messages import TrainOrderMessage
from darwinpush.messages.TrainOrderMessage import Action as TrainOrderAction

class TestTrainOrderMessage:

    def get_train_order_message_from_file(self, file_path):
        with open(file_path) as f:
            x = f.read()
            r = pp.CreateFromDocument(x)
            assert(None is r.sR)
            assert(None is not r.uR)
            assert(1 == len(r.uR.trainOrder))

            s = TrainOrderMessage(r.uR.trainOrder[0], r, x)
            return s

    def test_train_order_message(self):
        m = self.get_train_order_message_from_file("tests/data/train_order_message.xml")
        assert(None is not m)

        assert("TULSEH" == m.tiploc)
        assert("TUH" == m.crs)
        assert("2" == m.platform)
        assert(TrainOrderAction.Set == m.action)
        assert(None is not m.first)
        assert(None is m.second)
        assert(None is m.third)

        f = m.first
        assert("201505281285165" == f.rid)
        assert(None is f.headcode)
        assert(datetime.time(12, 15) == f.working_arrival_time)
        assert(None is f.working_pass_time)
        assert(datetime.time(12, 16, 30) == f.working_departure_time)
        assert(datetime.time(12, 15) == f.public_arrival_time)
        assert(datetime.time(12, 16) == f.public_departure_time)

    def test_train_order_message_departure_only(self):
        m = self.get_train_order_message_from_file("tests/data/train_order_message__departure_only.xml")
        assert(None is not m)

        assert("EPSM" == m.tiploc)
        assert("EPS" == m.crs)
        assert("1" == m.platform)
        assert(TrainOrderAction.Set == m.action)
        assert(None is not m.first)
        assert(None is m.second)
        assert(None is m.third)

        f = m.first
        assert("201505281285618" == f.rid)
        assert(None is f.headcode)
        assert(None is f.working_arrival_time)
        assert(None is f.working_pass_time)
        assert(datetime.time(14, 49) == f.working_departure_time)
        assert(None is f.public_arrival_time)
        assert(datetime.time(14, 49) == f.public_departure_time)

    @pytest.mark.xfail
    def test_train_order_message_clear(self):
        # This test requires an example of a TrainOrder Clear message in order to implement it.
        assert(False)
    
    @pytest.mark.xfail
    def test_train_order_message_headcode(self):
        # This test requires an example of a TrainOrder message with the service identified by
        # a headcode in order to implement it.
        assert(False)

    @pytest.mark.xfail
    def test_train_order_message_second_and_third(self):
        # This test requires an example of a TrainOrder message with all three services populated
        # in order to implement it.
        assert(False)

    @pytest.mark.xfail
    def test_train_order_datetime_timezone(self):
        # This test requires the code to be implemented that allows for tz aware date-time-ifying
        # of the times in this object, by combining them with the relevant tz-and-date-ified
        # ScheduleMessage objects.
        assert(False)


