from darwinpush.messages.BaseMessage import BaseMessage

import enum

class Action(enum.Enum):
    Set = 1
    Clear = 2


class Type(enum.Enum):
    TdAreaFail = 1
    TdFeedFail = 2
    TyrellFeedFail = 3


class UnknownAlarmTypeError(Exception):
    pass


class AlarmMessage(BaseMessage):
    
    def __init__(self, raw, containing_message, xml):
        super().__init__(raw, containing_message, xml)
        self._extract_alarm_data()

    def _extract_alarm_data(self):
        # Work out the alrm action.
        if self.raw.clear is not None:
            self._alarm_action = Action.Clear
            self._alarm_type = None
            self._alarm_id = int(self.raw.clear)
        elif self.raw.set_ is not None:
            self._raw_alarm = self.raw.set_
            self._alarm_action= Action.Set
            self._alarm_id = int(self._raw_alarm.id)
            if self._raw_alarm.tdAreaFail is not None:
                self._raw_alarm_payload = self._raw_alarm.tdAreaFail
                self._alarm_type = Type.TdAreaFail
            elif self._raw_alarm.tdFeedFail is not None:
                self._raw_alarm_payload = self._raw_alarm.tdFeedFail
                self._alarm_type = Type.TdFeedFail
            elif self._raw_alarm.tyrellFeedFail is not None:
                self._raw_alarm_payload = self._raw_alarm.tyrellFeedFail
                self._alarm_type = Type.TyrellFeedFail
            else:
                raise UnknownAlarmTypeError("Unknown Alarm Type encountered. All known types were None: {}".format(self.xml))
        else:
            raise UnknownAlarmActionError("Unknown Alarm Action encountered. All known actions were None: {}".format(self.xml))

    @property
    def alarm_action(self):
        return self._alarm_action

    @property
    def alarm_type(self):
        return self._alarm_type

    @property
    def aid(self):
        return self._alarm_id

    


