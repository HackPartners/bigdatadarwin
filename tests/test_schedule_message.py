import os
import sys
sys.path.append(os.getcwd())

import datetime
import pytest
import pytz

import darwinpush.xb.pushport as pp
from darwinpush.messagefactories.xml import ScheduleXMLMessageFactory

class TestScheduleMessage:
    
    def get_schedule_message_from_file(self, file_path):
        with open(file_path) as f:
            x = f.read()
            r = pp.CreateFromDocument(x)
            assert(None is r.sR)
            assert(None is not r.uR)
            assert(1 == len(r.uR.schedule))
            
            s = ScheduleXMLMessageFactory.build(r.uR.schedule[0], r, x)
            return s
         
    def test_schedule_message(self):
        m = self.get_schedule_message_from_file("tests/data/schedule_message.xml")
        assert(None is not m)

        # Check the basic message properties.
        assert("L06990" == m.uid)
        assert("201507202885757" == m.rid)
        assert("2W40" == m.headcode)
        assert(datetime.date(2015, 7, 20) == m.start_date)
        assert("TL" == m.toc_code)
        assert(True is m.passenger_service)
        assert("P" == m.status)
        assert("OO" == m.category)
        assert(True is m.active)
        assert(False is m.deleted)
        assert(False is m.charter)
        assert(None is m.cancel_reason)

        # Check the size of the list properties.
        assert(1 == len(m.origins))
        assert(0 == len(m.operational_origins))
        assert(13 == len(m.intermediate_points))
        assert(0 == len(m.operational_intermediate_points))
        assert(40 == len(m.passing_points))
        assert(1 == len(m.destinations))
        assert(0 == len(m.operational_destinations))

        # Check the properties of an origin.
        i = m.origins[0]
        assert("THBDGS" == i.tiploc)
        assert("TB" == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(None is i.route_delay)

        assert(None is i.working_arrival_time is None)
        assert(None is i.public_arrival_time is None)
        assert(None is i.working_pass_time is None)
        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 44)) == i.public_departure_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 44)) == i.working_departure_time)

        # Check the properties of a passing point.
        i = m.passing_points[0]
        assert("TNSLYGJ" == i.tiploc)
        assert("  " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(None is i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 46, 20)) == i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(None is i.working_departure_time)

        # Check the properties of an intermediate point.
        i = m.intermediate_points[0]
        assert("GTWK" == i.tiploc)
        assert("T " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 47, 30)) == i.working_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 48)) == i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 49)) == i.public_departure_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 12, 49)) == i.working_departure_time)

        # Check the properties of a destination.
        i = m.destinations[0]
        assert("BEDFDM" == i.tiploc)
        assert("TF" == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 14, 49)) == i.working_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 7, 20, 14, 49)) == i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(None is i.working_departure_time)

    def test_schedule_message_cross_midnight(self):
        m = self.get_schedule_message_from_file("tests/data/schedule_message__cross_midnight.xml")
        assert(None is not m)

        # Check the basic message properties.
        assert("P00313" == m.uid)
        assert("201508073420057" == m.rid)
        assert("1B94" == m.headcode)
        assert(datetime.date(2015, 8, 7) == m.start_date)
        assert("GW" == m.toc_code)
        assert(True is m.passenger_service)
        assert("P" == m.status)
        assert("XX" == m.category)
        assert(True is m.active)
        assert(False is m.deleted)
        assert(False is m.charter)
        assert(None is m.cancel_reason)

        # Check the size of the list properties.
        assert(1 == len(m.origins))
        assert(0 == len(m.operational_origins))
        assert(9 == len(m.intermediate_points))
        assert(0 == len(m.operational_intermediate_points))
        assert(40 == len(m.passing_points))
        assert(1 == len(m.destinations))
        assert(0 == len(m.operational_destinations))

        # Check the properties of an origin.
        i = m.origins[0]
        assert("PADTON" == i.tiploc)
        assert("TB" == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(None is i.route_delay)

        assert(None is i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 21, 45)) == i.public_departure_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 21, 45)) == i.working_departure_time)

        # Check the properties of a passing point.
        i = m.passing_points[0]
        assert("LDBRKJ" == i.tiploc)
        assert("  " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(None is i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 21, 48, 30)) == i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(None is i.working_departure_time)

        # Check the properties of a passing point after midnight (local time) but before in UTC
        i = m.passing_points[35]
        assert("MSHFILD" == i.tiploc)
        assert("  " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(None is i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 23, 48, 30)) == i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(None is i.working_departure_time)

        # Check the properties of a passing point after midnight (local time and UTC).
        i = m.passing_points[38]
        assert("MRGMMJN" == i.tiploc)
        assert("  " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(None is i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 8, 0, 29, 0)) == i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(None is i.working_departure_time)

        # Check the properties of an intermediate point.
        i = m.intermediate_points[0]
        assert("RDNGSTN" == i.tiploc)
        assert("T " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 22, 11, 0)) == i.working_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 22, 9, 0)) == i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 22, 11, 0)) == i.public_departure_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 22, 13, 0)) == i.working_departure_time)

        # Check the properties of an intermediate point after midnight (local time) but before in UTC
        i = m.intermediate_points[3]
        assert("BRSTPWY" == i.tiploc)
        assert("T " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 23, 15, 30)) == i.working_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 23, 15, 0)) == i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 23, 16, 0)) == i.public_departure_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 7, 23, 17, 30)) == i.working_departure_time)

        # Check the properties of an intermediate point after midnight (local & UTC).
        i = m.intermediate_points[6]
        assert("BRGEND" == i.tiploc)
        assert("T " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(pytz.utc.localize(datetime.datetime(2015, 8, 8, 0, 20, 0)) == i.working_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 8, 0, 20, 0)) == i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 8, 0, 22, 0)) == i.public_departure_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 8, 0, 22, 0)) == i.working_departure_time)

        # Check the properties of a destination.
        i = m.destinations[0]
        assert("SWANSEA" == i.tiploc)
        assert("TF" == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(pytz.utc.localize(datetime.datetime(2015, 8, 8, 0, 56)) == i.working_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 8, 0, 56)) == i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(None is i.working_departure_time)

    def test_schedule_message_not_passenger(self):
        m = self.get_schedule_message_from_file("tests/data/schedule_message__not_passenger.xml")
        assert(m is not None)

        # Check the basic message properties.
        assert("Y58074" == m.uid)
        assert("201508093490803" == m.rid)
        assert("5S23" == m.headcode)
        assert(datetime.date(2015, 8, 9) == m.start_date)
        assert("GR" == m.toc_code)
        assert(False is m.passenger_service)
        assert("P" == m.status)
        assert("EE" == m.category)
        assert(True is m.active)
        assert(False is m.deleted)
        assert(False is m.charter)
        assert(None is m.cancel_reason)

        # Check the size of the list properties.
        assert(0 == len(m.origins))
        assert(1 == len(m.operational_origins))
        assert(0 == len(m.intermediate_points))
        assert(1 == len(m.operational_intermediate_points))
        assert(1 == len(m.passing_points))
        assert(0 == len(m.destinations))
        assert(1 == len(m.operational_destinations))

        # Check the properties of an operational origin.
        i = m.operational_origins[0]
        assert("EDINBUR" == i.tiploc)
        assert("TB" == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(None is i.route_delay)

        assert(None is i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 9, 19, 40)) == i.working_departure_time)

        # Check the properties of a passing point.
        i = m.passing_points[0]
        assert("ABHLJN" == i.tiploc)
        assert("  " == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(None is i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 9, 19, 42)) == i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(None is i.working_departure_time)

        # Check the properties of an operational intermediate point.
        i = m.operational_intermediate_points[0]
        assert("CRGNTYJ" == i.tiploc)
        assert("OP" == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(pytz.utc.localize(datetime.datetime(2015, 8, 9, 19, 44)) == i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(pytz.utc.localize(datetime.datetime(2015, 8, 9, 19, 44, 30)) == i.working_departure_time)

        # Check the properties of an operational destination.
        i = m.operational_destinations[0]
        assert("CRGNTNY" == i.tiploc)
        assert("TF" == i.activity_codes)
        assert(None is i.planned_activity_codes)
        assert(False is i.cancelled)
        assert(None is i.false_tiploc)
        assert(0 == i.route_delay)

        assert(pytz.utc.localize(datetime.datetime(2015, 8, 9, 19, 48)) == i.working_arrival_time)
        assert(None is i.public_arrival_time)
        assert(None is i.working_pass_time)
        assert(None is i.public_departure_time)
        assert(None is i.working_departure_time)

    @pytest.mark.xfail
    def test_schedule_message_multiple_origins(self):
        # Need an example ScheduleMessage with multiple origins. Is this even possible?
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_multiple_destinations(self):
        # Need an example ScheduleMessage with multiple destinations. Is this even possible?
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_spring_forward(self):
        # Need to cover all our bases for schedules that cross the "Spring Forward" boundary
        # primarily to make sure the tz aware datetime determination works properly.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_fall_back(self):
        # Need to cover all our bases for schedules that cross the "Fall Back" boundary
        # primarily to make sure the tz aware datetime determination works properly.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_gmt(self):
        # All the other test schedules use BST time. Need a test to make sure GMT ones work fine too.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_deleted(self):
        # Need an example of a ScheudleMessage that is deleted.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_cancelled(self):
        # Need an example of a ScheduleMessage that is cancelled at some calling point.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_false_tiploc(self):
        # Need an example of a ScheduleMessage with a false tiploc at some calling point.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_route_delay(self):
        # Need an example of a ScheduleMessage with a route delay at some calling point.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_active(self):
        # Need an example of a ScheduleMessage that is not active in Darwin.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_charter(self):
        # Need an example of a ScheduleMessage that is a charter train.
        assert(False)

    @pytest.mark.xfail
    def test_schedule_message_cancel_reason(self):
        # Need an example of a ScheduleMessage that has a cancel reason.
        assert(False)


