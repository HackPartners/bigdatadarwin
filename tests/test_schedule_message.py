import os
import sys
sys.path.append(os.getcwd())

import datetime
import pytest
import pytz

import darwinpush.xb.pushport as pp
from darwinpush.messages import ScheduleMessage

class TestScheduleMessage:
    
    def get_schedule_message_from_file(self, file_path):
        with open(file_path) as f:
            r = pp.CreateFromDocument(f.read())
            assert(r.sR is None)
            assert(r.uR is not None)
            assert(len(r.uR.schedule) == 1)
            
            s = ScheduleMessage(r.uR.schedule[0], r)
            return s
         
    def test_schedule_message(self):
        m = self.get_schedule_message_from_file("tests/data/schedule_message.xml")
        assert(m is not None)

        # Check the basic message properties.
        assert(m.uid == "L06990")
        assert(m.rid == "201507202885757")
        assert(m.headcode == "2W40")
        assert(m.start_date == datetime.date(2015, 7, 20))
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

        # Check the properties of an origin.
        i = m.origins[0]
        assert(i.tiploc == "THBDGS")
        assert(i.activity_codes == "TB")
        assert(i.planned_activity_codes is None)
        assert(i.cancelled == False)
        assert(i.false_tiploc is None)
        assert(i.route_delay is None)

        assert(i.working_arrival_time is None)
        assert(i.public_arrival_time is None)
        assert(i.working_pass_time is None)
        assert(i.public_departure_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 44)))
        assert(i.working_departure_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 44)))

        # Check the properties of a passing point.
        i = m.passing_points[0]
        assert(i.tiploc == "TNSLYGJ")
        assert(i.activity_codes == "  ")
        assert(i.planned_activity_codes is None)
        assert(i.cancelled == False)
        assert(i.false_tiploc is None)
        assert(i.route_delay == 0)

        assert(i.working_arrival_time is None)
        assert(i.public_arrival_time is None)
        assert(i.working_pass_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 46, 20)))
        assert(i.public_departure_time is None)
        assert(i.working_departure_time is None)

        # Check the properties of an intermediate point.
        i = m.intermediate_points[0]
        assert(i.tiploc == "GTWK")
        assert(i.activity_codes == "T ")
        assert(i.planned_activity_codes is None)
        assert(i.cancelled == False)
        assert(i.false_tiploc is None)
        assert(i.route_delay == 0)

        assert(i.working_arrival_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 47, 30)))
        assert(i.public_arrival_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 48)))
        assert(i.working_pass_time is None)
        assert(i.public_departure_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 49)))
        assert(i.working_departure_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 49)))

        # Check the properties of a destination.
        i = m.destinations[0]
        assert(i.tiploc == "BEDFDM")
        assert(i.activity_codes == "TF")
        assert(i.planned_activity_codes is None)
        assert(i.cancelled == False)
        assert(i.false_tiploc is None)
        assert(i.route_delay == 0)

        assert(i.working_arrival_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 14, 49)))
        assert(i.public_arrival_time == pytz.utc.localize(datetime.datetime(2015, 7, 20, 14, 49)))
        assert(i.working_pass_time is None)
        assert(i.public_departure_time is None)
        assert(i.working_departure_time is None)


