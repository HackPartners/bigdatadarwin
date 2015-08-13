from darwinpush.messages.TrainStatusMessage import *

from dateutil.parser import *

class TrainStatusXMLMessageFactory:

    @staticmethod
    def build(raw, containing_message, xml):
        m = TrainStatusMessage()

        if raw.LateReason is not None:
            m.late_reason = f.build_late_reason(raw.LateReason)
        else:
            m.late_reason = None

        m.locations = []
        for l in raw.Location:
            m.locations.append(f.build_location(l))

        m.rid = raw.rid
        m.uid = raw.uid
        m.start_date = raw.ssd.date()
        m.reverse_formation = bool(raw.isReverseFormation)

        m._raw = raw
        m._containing_message = containing_message
        m._xml = xml

        return m

    @staticmethod
    def build_late_reason(raw):
        r = LateReason()

        r.code = raw.value()
        r.tiploc = raw.tiploc
        r.near = bool(raw.near)

        return r

    @staticmethod
    def build_location(raw):
        r = Location()

        r.forecast_arrival_time = f.build_forecast(raw.arr)
        r.forecast_departure_time = f.build_forecast(raw.dep)
        r.forecast_pass_time = f.build_forecast(raw.pass_)
        r.platform = f.build_platform(raw.plat)
        r.suppressed = raw.suppr
        r.length = raw.length
        r.detach_front = raw.detachFront
        r.working_arrival_time = f.build_time(raw.wta)
        r.working_departure_time = f.build_time(raw.wtd)
        r.working_pass_time = f.build_time(raw.wtp)
        r.public_arrival_time = f.build_time(raw.pta)
        r.public_departure_time = f.build_time(raw.ptd)
        r.tiploc = raw.tpl

        return r

    @staticmethod
    def build_forecast(raw):
        if raw is None:
            return None

        r = Forecast()

        r.estimated_time = f.build_time(raw.et)
        r.working_estimated_time = f.build_time(raw.wet)
        r.actual_time = f.build_time(raw.at)
        r.actual_time_removed = raw.atRemoved
        r.manual_estimate_lower_limit_minutes = raw.etmin
        r.manual_estimate_unknown_delay = raw.etUnknown
        r.unknown_delay = raw.delayed
        r.source = raw.src
        r.source_cis = raw.srcInst

        return r

    @staticmethod
    def build_platform(raw):
        if raw is None:
            return None

        r = Platform()

        r.suppressed = bool(raw.platsup)
        r.suppressed_by_cis = bool(raw.cisPlatsup)
        r.source = raw.platsrc
        r.confirmed = bool(raw.conf)
        r.number = raw.value()

        return r

    @staticmethod
    def build_time(raw):
        if raw is None:
            return None
        return parse(raw).time()

f = TrainStatusXMLMessageFactory


