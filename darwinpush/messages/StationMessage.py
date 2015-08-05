from darwinpush.messages.BaseMessage import BaseMessage

from darwinpush.xb.sm import MsgCategoryType, MsgSeverityType

import enum

class UnknownStationMessageCategoryError(Exception):
    pass


class UnknownStationMessageSeverityError(Exception):
    pass


class StationMessageCategory(enum.Enum):
    Train = 0
    Station = 1
    Connection = 2
    System = 3
    Misc = 4
    PriorTrain = 5
    PriorOther = 6

    @staticmethod
    def from_xb(x):
        if x == MsgCategoryType.Train:
            return StationMessageCategory.Train
        if x == MsgCategoryType.Station:
            return StationMessageCategory.Station
        if x == MsgCategoryType.Connections:
            return StationMessageCategory.Connection
        if x == MsgCatgoryType.System:
            return StationMessageCategory.System
        if x == MsgCategoryType.Misc:
            return StationMessageCategory.Misc
        if x == MsgCategoryType.PriorTrains:
            return StationMessageCategory.PriorTrain
        if x == MsgCategoryType.PriorOther:
            return StationMessageType.PriorOther

        raise UnknownStationMessageCategoryError("Unknown Station Message Category '{}' received in Station Message.".format(x))


class StationMessageSeverity(enum.Enum):
    LevelZero = 0
    LevelOne = 1
    LevelTwo = 2
    LevelThree = 3

    @staticmethod
    def from_xb(x):
        if x == MsgSeverityType.n0:
            return StationMessageSeverity.LevelZero
        if x == MsgSeverityType.n1:
            return StationMessageSeverity.LevelOne
        if x == MsgSeverityType.n2:
            return StationMessageSeverity.LevelTwo
        if x == MsgSeverityType.n3:
            return StationMessageSeverity.LevelThree

        raise UnknownStationMessageSeverityError("Unknown Station Message Severity '{}' received in Station Message.".format(x))


class StationMessage(BaseMessage):

    def __init__(self, message, containing_message):
        super().__init__(message, containing_message)
        self._build_stations_list()

    def _build_stations_list(self):
        self._stations = []
        for s in self.raw.Station:
            self._stations.append(s.crs)

    @property
    def stations(self):
        return self._stations

    @property
    def message(self):
        return self.raw.Msg.orderedContent()[0].value

    @property
    def smid(self):
        return self.raw.id

    @property
    def category(self):
        return StationMessageCategory.from_xb(self.raw.cat)

    @property
    def severity(self):
        return StationMessageSeverity.from_xb(self.raw.sev)


