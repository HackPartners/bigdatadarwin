import os
import sys
sys.path.append(os.getcwd())

import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messages import AlarmMessage
from darwinpush.messages.AlarmMessage import Type as AlarmType, Action as AlarmAction

class TestAlarmMessage:

    def get_alarm_message_from_file(self, file_path):
        with open(file_path) as f:
            x = f.read()
            r = pp.CreateFromDocument(x)
            assert(None is r.sR)
            assert(None is not r.uR)
            assert(1 == len(r.uR.alarm))

            s = AlarmMessage(r.uR.alarm[0], r, x)
            return s

    def test_alarm_message(self):
        m = self.get_alarm_message_from_file("tests/data/alarm_message.xml")
        assert(None is not m)

        assert(AlarmAction.Set == m.alarm_action)
        assert(AlarmType.TyrellFeedFail == m.alarm_type)
        assert(39607 == m.aid)

    def test_alarm_message_clear(self):
        m = self.get_alarm_message_from_file("tests/data/alarm_message__clear.xml")
        assert(None is not m)

        assert(AlarmAction.Clear == m.alarm_action)
        assert(None is m.alarm_type)
        assert(39607 == m.aid)

    # This test is expected to fail until we have a correct example of this alarm type in the data.
    @pytest.mark.xfail
    def test_alarm_message_tdfeedfail(self):
        m = self.get_alarm_message_from_file("tests/data/alarm_message__tdfeedfail.xml")
        assert(None is not m)

        assert(AlarmAction.Set == m.alarm_action)
        assert(AlarmType.TdFeedFail == m.alarm_type)
        assert(39432 == m.aid)


    
