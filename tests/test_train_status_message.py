import os
import sys
sys.path.append(os.getcwd())

import datetime
import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messages import TrainStatusMessage
from darwinpush.messagefactories.xml import TrainStatusXMLMessageFactory

class TestTrainStatusMessage:

    def get_train_status_message_from_file(self, file_path):
        with open(file_path) as f:
            x = f.read()
            r = pp.CreateFromDocument(x)
            assert(None is r.sR)
            assert(None is not r.uR)
            assert(1 == len(r.uR.TS))

            s = TrainStatusXMLMessageFactory.build(r.uR.TS[0], r, x)
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
    
    def test_train_status_message_platform_suppressed(self):
        m = self.get_train_status_message_from_file("tests/data/train_status_message__plat_sup.xml")
        assert(None is not m)

        assert("201508113548457" == m.rid)
        assert("G00192" == m.uid)
        assert(datetime.date(2015, 8, 11) == m.start_date)
        assert(None is m.late_reason)
        assert(1 == len(m.locations))
        assert(False is m.reverse_formation)

        l = m.locations[0]
        assert(None is not l)
        assert(None is l.forecast_arrival_time)
        assert(None is l.forecast_departure_time)
        assert(None is not l.forecast_pass_time)
        assert(None is not l.platform)
        assert(None is l.suppressed)
        assert(None is l.length)
        assert(None is l.detach_front)
        assert(None is l.working_arrival_time)
        assert(None is l.working_departure_time)
        assert(datetime.time(22, 5, 30) == l.working_pass_time)
        assert(None is l.public_arrival_time)
        assert(None is l.public_departure_time)
        assert("BROXBRN" == l.tiploc)

        t = l.forecast_pass_time
        assert(None is not t)
        assert(None is t.estimated_time)
        assert(None is t.working_estimated_time)
        assert(datetime.time(22, 6) == t.actual_time)
        assert(0 == t.actual_time_removed)
        assert(None is t.manual_estimate_lower_limit_minutes)
        assert(0 == t.manual_estimate_unknown_delay)
        assert(0 == t.unknown_delay)
        assert("TD" == t.source)
        assert(None is t.source_cis)
    
        p = l.platform
        assert(None is not l.platform)
        assert(True is p.suppressed)
        assert(True is p.suppressed_by_cis)
        assert("P" == p.source)
        assert(False is p.confirmed)
        assert("2" == p.number)

    def test_train_status_message_at_station(self):
        m = self.get_train_status_message_from_file("tests/data/train_status_message__at_station.xml")
        assert(None is not m)

        assert("201508113549417" == m.rid)
        assert("W22143" == m.uid)
        assert(datetime.date(2015, 8, 11) == m.start_date)
        assert(None is m.late_reason)
        assert(2 == len(m.locations))
        assert(False is m.reverse_formation)

        l = m.locations[0]
        assert(None is not l)
        assert(None is not l.forecast_arrival_time)
        assert(None is not l.forecast_departure_time)
        assert(None is l.forecast_pass_time)
        assert(None is not l.platform)
        assert(None is l.suppressed)
        assert(None is l.length)
        assert(None is l.detach_front)
        assert(datetime.time(22, 5, 30) == l.working_arrival_time)
        assert(datetime.time(22, 6) == l.working_departure_time)
        assert(None is l.working_pass_time)
        assert(datetime.time(22, 6) == l.public_arrival_time)
        assert(datetime.time(22, 6) == l.public_departure_time)
        assert("CATFBDG" == l.tiploc)

        t = l.forecast_arrival_time
        assert(None is not t)
        assert(None is t.estimated_time)
        assert(None is t.working_estimated_time)
        assert(datetime.time(22, 5) == t.actual_time)
        assert(0 == t.actual_time_removed)
        assert(None is t.manual_estimate_lower_limit_minutes)
        assert(0 == t.manual_estimate_unknown_delay)
        assert(0 == t.unknown_delay)
        assert("TD" == t.source)
        assert(None is t.source_cis)

        t = l.forecast_departure_time
        assert(None is not t)
        assert(datetime.time(22, 6) == t.estimated_time)
        assert(None is t.working_estimated_time)
        assert(None is t.actual_time)
        assert(0 == t.actual_time_removed)
        assert(None is t.manual_estimate_lower_limit_minutes)
        assert(0 == t.manual_estimate_unknown_delay)
        assert(0 == t.unknown_delay)
        assert("Darwin" == t.source)
        assert(None is t.source_cis)
    
        p = l.platform
        assert(None is not l.platform)
        assert(False is p.suppressed)
        assert(False is p.suppressed_by_cis)
        assert("A" == p.source)
        assert(True is p.confirmed)
        assert("2" == p.number)

        l = m.locations[1]
        assert(None is not l)
        assert(None is not l.forecast_arrival_time)
        assert(None is not l.forecast_departure_time)
        assert(None is l.forecast_pass_time)
        assert(None is not l.platform)
        assert(None is l.suppressed)
        assert(None is l.length)
        assert(None is l.detach_front)
        assert(datetime.time(22, 8, 30) == l.working_arrival_time)
        assert(datetime.time(22, 9) == l.working_departure_time)
        assert(None is l.working_pass_time)
        assert(datetime.time(22, 9) == l.public_arrival_time)
        assert(datetime.time(22, 9) == l.public_departure_time)
        assert("LSYDNHM" == l.tiploc)

        t = l.forecast_arrival_time
        assert(None is not t)
        assert(datetime.time(22, 9) == t.estimated_time)
        assert(datetime.time(22, 8) == t.working_estimated_time)
        assert(None is t.actual_time)
        assert(0 == t.actual_time_removed)
        assert(None is t.manual_estimate_lower_limit_minutes)
        assert(0 == t.manual_estimate_unknown_delay)
        assert(0 == t.unknown_delay)
        assert("Darwin" == t.source)
        assert(None is t.source_cis)

        t = l.forecast_departure_time
        assert(None is not t)
        assert(datetime.time(22, 9) == t.estimated_time)
        assert(None is t.working_estimated_time)
        assert(None is t.actual_time)
        assert(0 == t.actual_time_removed)
        assert(None is t.manual_estimate_lower_limit_minutes)
        assert(0 == t.manual_estimate_unknown_delay)
        assert(0 == t.unknown_delay)
        assert("Darwin" == t.source)
        assert(None is t.source_cis)
    
        p = l.platform
        assert(None is not l.platform)
        assert(False is p.suppressed)
        assert(False is p.suppressed_by_cis)
        assert("A" == p.source)
        assert(True is p.confirmed)
        assert("2" == p.number)

    def test_train_status_message_length(self):
        m = self.get_train_status_message_from_file("tests/data/train_status_message__length.xml")
        assert(None is not m)

        assert("201508113555894" == m.rid)
        assert("W83145" == m.uid)
        assert(datetime.date(2015, 8, 11) == m.start_date)
        assert(None is m.late_reason)
        assert(1 == len(m.locations))
        assert(False is m.reverse_formation)

        l = m.locations[0]
        assert(None is not l)
        assert(None is not l.forecast_arrival_time)
        assert(None is l.forecast_departure_time)
        assert(None is l.forecast_pass_time)
        assert(None is not l.platform)
        assert(None is l.suppressed)
        assert(4 == l.length)
        assert(None is l.detach_front)
        assert(datetime.time(22, 5) == l.working_arrival_time)
        assert(None is l.working_departure_time)
        assert(None is l.working_pass_time)
        assert(datetime.time(22, 5) == l.public_arrival_time)
        assert(None is l.public_departure_time)
        assert("PHBR" == l.tiploc)

        t = l.forecast_arrival_time
        assert(None is not t)
        assert(datetime.time(22, 8) == t.estimated_time)
        assert(None is t.working_estimated_time)
        assert(None is t.actual_time)
        assert(0 == t.actual_time_removed)
        assert(None is t.manual_estimate_lower_limit_minutes)
        assert(0 == t.manual_estimate_unknown_delay)
        assert(0 == t.unknown_delay)
        assert("TD" == t.source)
        assert(None is t.source_cis)
    
        p = l.platform
        assert(None is not l.platform)
        assert(False is p.suppressed)
        assert(False is p.suppressed_by_cis)
        assert("P" == p.source)
        assert(False is p.confirmed)
        assert("3" == p.number)


