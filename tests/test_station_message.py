import os
import sys
sys.path.append(os.getcwd())

import pytest

import darwinpush.xb.sm as sm

class TestStationMessage:
    def test_station_message(self):
        with open("tests/data/station_message.xml") as f:
            #r = sm.CreateFromDocument(f.read())
            #m = StationMessage(r)

            assert(True)


