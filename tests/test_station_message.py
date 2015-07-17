import os
import sys
sys.path.append(os.getcwd())

import pytest

import pyxb.utils.domutils as domutils

import darwinpush.xb.sm as sm

class TestStationMessage:
    def test_station_message(self):
        with open("tests/data/station_message.xml") as f:
            doc = domutils.StringToDOM(f.read())
            r = sm.CreateFromDOM(doc)
            m = StationMessage(r)

            assert(True)


