import os
import sys
sys.path.append(os.getcwd())

import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messages import StationMessage
from darwinpush.messages.StationMessage import StationMessageCategory, StationMessageSeverity

class TestStationMessage:

    def get_station_message_from_file(self, file_path):
        with open(file_path) as f:
            r = pp.CreateFromDocument(f.read())
            assert(r.sR is None)
            assert(r.uR is not None)
            assert(len(r.uR.OW) == 1)

            s = StationMessage(r.uR.OW[0], r)
            return s

    def test_station_message(self):
        m = self.get_station_message_from_file("tests/data/station_message.xml")
        assert(None is not m)

        assert(1 == len(m.stations))
        assert("BSK" == m.stations[0])
        assert("The lifts on platforms 2 and 3 at Basingstoke will be out of use until at least September 2015. " == m.message)
        assert(51504 == m.smid)
        assert(StationMessageCategory.Station == m.category)
        assert(StationMessageSeverity.LevelOne == m.severity)


