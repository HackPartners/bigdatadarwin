from darwinpush.messages.BaseMessage import BaseMessage

from dateutil.parser import *

class LateReason:

    def __init__(self, raw):
        self.raw = raw

    @property
    def code(self):
        return self.raw.value()

    @property
    def tiploc(self):
        return self.raw.tiploc

    """
    True if the TIPLOC property should be interpreted as "near" instead of "at", otherwise False.
    e.g. "Signal Failure near Plymouth" instead of "Signal Failure at Plymouth"
    """
    @property
    def near(self):
        return bool(self.raw.near)

    def __repr__(self):
        return "LateReason({},{},{})".format(self.code, self.tiploc, self.near)


class Location:

    def __init__(self, raw):
        self.raw = raw

    @property
    def forecast_arrival_time(self):
        if self.raw.arr is None:
            return None
        return Forecast(self.raw.arr)

    @property
    def forecast_departure_time(self):
        if self.raw.dep is None:
            return None
        return Forecast(self.raw.dep)

    @property
    def forecast_pass_time(self):
        if self.raw.pass_ is None:
            return None
        return Forecast(self.raw.pass_)

    @property
    def platform(self):
        return self.raw.plat

    @property
    def suppressed(self):
        return self.raw.suppr

    @property
    def length(self):
        return self.raw.length

    @property
    def detach_front(self):
        return self.raw.detachFront

    @property
    def working_arrival_time(self):
        if self.raw.wta is None:
            return None
        return parse(self.raw.wta).time()

    @property
    def working_departure_time(self):
        if self.raw.wtd is None:
            return None
        return parse(self.raw.wtd).time()

    @property
    def working_pass_time(self):
        if self.raw.wtp is None:
            return None
        return parse(self.raw.wtp).time()

    @property
    def public_arrival_time(self):
        if self.raw.pta is None:
            return None
        return parse(self.raw.pta).time()

    @property
    def public_departure_time(self):
        if self.raw.ptd is None:
            return None
        return parse(self.raw.ptd).time()

    @property
    def tiploc(self):
        return self.raw.tpl


class Forecast:

    def __init__(self, raw):
        self.raw = raw

    @property
    def estimated_time(self):
        if self.raw.et is None:
            return None
        return parse(self.raw.et).time()

    @property
    def working_estimated_time(self):
        if self.raw.wet is None:
            return None
        return parse(self.raw.wet).time()

    @property
    def actual_time(self):
        if self.raw.at is None:
            return None
        return parse(self.raw.at).time()

    @property
    def actual_time_removed(self):
        return self.raw.atRemoved

    @property
    def manual_estimate_lower_limit_minutes(self):
        return self.raw.etmin

    @property
    def manual_estimate_unknown_delay(self):
        return self.raw.etUnknown

    @property
    def unknown_delay(self):
        return self.raw.delayed

    @property
    def source(self):
        return self.raw.src

    @property
    def source_cis(self):
        return self.raw.srcInst


class TrainStatusMessage(BaseMessage):

    def __init__(self, raw, containing_message, xml):
        super().__init__(raw, containing_message, xml)
        self._make_late_reason()
        self._make_locations()
    
    def _make_late_reason(self):
        if self.raw.LateReason is not None:
            self._late_reason = LateReason(self.raw.LateReason)
        else:
            self._late_reason = None

    def _make_locations(self):
        self._locations = []
        for l in self.raw.Location:
            self._locations.append(Location(l))

    @property
    def late_reason(self):
        return self._late_reason
    
    @property
    def locations(self):
        return self._locations

    @property
    def rid(self):
        return self.raw.rid

    @property
    def uid(self):
        return self.raw.uid

    @property
    def start_date(self):
        return self.raw.ssd.date()

    @property
    def reverse_formation(self):
        return bool(self.raw.isReverseFormation)


