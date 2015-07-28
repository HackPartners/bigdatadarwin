import os
import sys
sys.path.append(os.getcwd())

import datetime
import pytest
import pytz

from darwinpush.utils import timezone_for_date_and_time

class TestUtcOffsetForDateAndTime:

    def test_uncontroversial_times(self):
        d = datetime.date(2015,1,5)
        t = datetime.time(18,30)

        assert(timezone_for_date_and_time(d,t) == pytz.timezone("Etc/GMT"))

        d = datetime.date(2015,6,5)
        t = datetime.time(21,00)

        assert(timezone_for_date_and_time(d,t) == pytz.timezone("Etc/GMT-1"))
    
    def test_spring_forward(self):
        d = datetime.date(2015,3,29)
        t = datetime.time(0,55)

        assert(timezone_for_date_and_time(d,t) == pytz.timezone("Etc/GMT"))

        d = datetime.date(2015,3,29)
        t = datetime.time(2,5)

        assert(timezone_for_date_and_time(d,t) == pytz.timezone("Etc/GMT-1"))

    def test_fall_back(self):
        d = datetime.date(2015,10,25)
        t = datetime.time(0,30)

        assert(timezone_for_date_and_time(d,t) == pytz.timezone("Etc/GMT-1"))

        d = datetime.date(2015,10,25)
        t = datetime.time(1,15)

        assert(timezone_for_date_and_time(d,t) == pytz.timezone("Etc/GMT"))

        d = datetime.date(2015,10,25)
        t = datetime.time(2,10)

        assert(timezone_for_date_and_time(d,t) == pytz.timezone("Etc/GMT"))


