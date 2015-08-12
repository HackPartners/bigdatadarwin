import os
import sys
sys.path.append(os.getcwd())

import datetime
import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messages import TrainStatusMessage

class TestTrainStatusMessage:

    def get_train_status_message_from_file(self, file_path):
        with open(file_path) as f:
            x = f.read()
            r = pp.CreateFromDocument(x)
            assert(None is r.sR)
            assert(None is not r.uR)
            assert(1 == len(r.uR.TS))

            s = TrainStatusMessage(r.uR.TS[0], r, x)
            return s

    def test_train_status_message(self):
        m = self.get_train_status_message_from_file("tests/data/train_status_message.xml")
        assert(None is not m)

        assert("201508123582133" == m.rid)
        assert("G00868" == m.uid)
        assert(datetime.date(2015, 8, 12) == m.start_date)
        assert(None is m.late_reason)
        assert(1 == len(m.locations))
        assert(False is m.reverse_formation)

    
    def test_train_status_message_late_reason_tiploc(self):
        m = self.get_train_status_message_from_file("tests/data/train_status_message__late_reason_tiploc.xml")
        assert(None is not m)

        assert("201508123594283" == m.rid)
        assert("L06321" == m.uid)
        assert(datetime.date(2015, 8, 12) == m.start_date)
        assert(1 == len(m.locations))
        assert(False is m.reverse_formation)

        l = m.late_reason
        assert(None is not l)
        assert(153 == l.code)
        assert("CRYSTLP" == l.tiploc)
        assert(False is l.near)

    def test_train_status_message_actual_time(self):
        m = self.get_train_status_message_from_file("tests/data/train_status_message__actual_time.xml")
        assert(None is not m)

        assert("201508113560355" == m.rid)
        assert("W84968" == m.uid)
        assert(datetime.date(2015, 8, 11) == m.start_date)
        assert(None is m.late_reason)
        assert(1 == len(m.locations))
        assert(False is m.reverse_formation)

        l = m.locations[0]
        assert(None is not l)
        assert(None is l.forecast_arrival_time)
        assert(None is l.forecast_departure_time)
        assert(None is not l.forecast_pass_time)
        assert(None is l.platform)
        assert(None is l.suppressed)
        assert(None is l.length)
        assert(None is l.detach_front)
        assert(None is l.working_arrival_time)
        assert(None is l.working_departure_time)
        assert(datetime.time(21, 59) == l.working_pass_time)
        assert(None is l.public_arrival_time)
        assert(None is l.public_departure_time)
        assert("STRENJN" == l.tiploc)

        t = l.forecast_pass_time
        assert(None is not t)
        assert(None is t.estimated_time)
        assert(None is t.working_estimated_time)
        assert(datetime.time(22, 1) == t.actual_time)
        assert(0 == t.actual_time_removed)
        assert(None is t.manual_estimate_lower_limit_minutes)
        assert(0 == t.manual_estimate_unknown_delay)
        assert(0 == t.unknown_delay)
        assert("TRUST" == t.source)
        assert("Auto" == t.source_cis)


