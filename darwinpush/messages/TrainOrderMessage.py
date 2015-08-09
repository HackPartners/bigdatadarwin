from darwinpush.messages.BaseMessage import BaseMessage

from dateutil.parser import *

import enum

class Action(enum.Enum):
    Set = 1
    Clear = 2


class UnknownTrainOrderActionError(Exception):
    pass


class TrainOrderItem():
    def __init__(self, raw):
        self._raw = raw

        try:
            self._working_arrival_time = parse(self.raw.rid.wta).time()
        except AttributeError:
            self._working_arrival_time = None

        try:
            self._working_departure_time = parse(self.raw.rid.wtd).time()
        except AttributeError:
            self._working_departure_time = None

        try:
            self._working_pass_time = parse(self.raw.rid.wtp).time()
        except AttributeError:
            self._working_pass_time = None

        try:
            self._public_arrival_time = parse(self.raw.rid.pta).time()
        except AttributeError:
            self._public_arrival_time = None

        try:
            self._public_departure_time = parse(self.raw.rid.ptd).time()
        except AttributeError:
            self._public_departure_time = None

    @property
    def raw(self):
        return self._raw

    @property
    def rid(self):
        return self.raw.rid.value()

    @property
    def headcode(self):
        return self.raw.trainID

    @property
    def working_arrival_time(self):
        return self._working_arrival_time

    @property
    def working_departure_time(self):
        return self._working_departure_time

    @property
    def working_pass_time(self):
        return self._working_pass_time

    @property
    def public_arrival_time(self):
        return self._public_arrival_time

    @property
    def public_departure_time(self):
        return self._public_departure_time


class TrainOrderMessage(BaseMessage):

    def __init__(self, raw, containing_message, xml):
        super().__init__(raw, containing_message, xml)
        self._determine_action()
        self._extract_train_order_data()

    def _determine_action(self):
        if self.raw.set_ is not None:
            self._action = Action.Set
        elif self.raw.clear is not None:
            self._action = Action.Clear
        else:
            raise UnknwonTrainOrderActionError("Unknown Train order Action encountered. All known actions were None: {}".format(self.xml))

    def _extract_train_order_data(self):
        if self.action != Action.Set:
            return

        if self.raw.set_.first is not None:
            self._first = TrainOrderItem(self.raw.set_.first)
        else:
            self._first = None

        if self.raw.set_.second is not None:
            self._second = TrainOrderItem(self.raw.set_.second)
        else:
            self._second = None

        if self.raw.set_.third is not None:
            self._third = TrainOrderItem(self.raw.set_.third)
        else:
            self._third = None

    @property
    def action(self):
        return self._action

    @property
    def tiploc(self):
        return self.raw.tiploc

    @property
    def crs(self):
        return self.raw.crs

    @property
    def platform(self):
        return self.raw.platform

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second

    @property
    def third(self):
        return self._third


