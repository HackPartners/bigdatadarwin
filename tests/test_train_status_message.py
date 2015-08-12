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


