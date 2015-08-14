from darwinpush.messages.ScheduleMessage import *

from dateutil.parser import *

from darwinpush.utils import timezone_for_date_and_time
from darwinpush.xb.raw.sch import OR, OPOR, IP, OPIP, PP, DT, OPDT
from darwinpush.xb.raw.ct import DisruptionReasonType

from datetime import datetime, timedelta
from dateutil.parser import *
import pytz

class ScheduleXMLMessageFactory:

    @staticmethod
    def build(raw, containing_message, xml):
        m = ScheduleMessage()

        m.uid = raw.uid
        m.rid = raw.rid
        m.headcode = raw.trainId
        m.start_date = raw.ssd.date()
        m.toc_code = raw.toc
        m.passenger_service = bool(raw.isPassengerSvc)
        m.status = raw.status
        m.category = raw.trainCat
        m.active = bool(raw.isActive)
        m.deleted = bool(raw.deleted)
        try:
            m.charter = bool(raw.charter)
        except AttributeError:
            m.charter = False
        if raw.cancelReason is not None:
            m.cancel_reason_code = raw.cancelReason.value()
            m.cancel_reason_tiploc = raw.cancelReason.tiploc
            m.cancel_reason_near = bool(raw.cancelReason.near)
        else:
            m.cancel_reason_code = None
            m.cancel_reason_tiploc = None
            m.cancel_reason_near = None

        # Loop through all the points in the order they appear in the XML, instantiate the
        # appropriate object for them, and add them to the appropriate list.
        m.origins = []
        m.operational_origins = []
        m.intermediate_points = []
        m.operational_intermediate_points = []
        m.passing_points = []
        m.destinations = []
        m.operational_destinations = []
        m.all_points = []

        for r in raw.orderedContent():
            v = r.value
            if type(v) == DisruptionReasonType:
                pass
            elif type(v) == OR:
                p = f.build_point(v, Origin)
                m.origins.append(p)
            elif type(v) == OPOR:
                p = f.build_point(v, OperationalOrigin)
                m.operational_origins.append(p)
            elif type(v) == IP:
                p = f.build_point(v, IntermediatePoint)
                m.intermediate_points.append(p)
            elif type(v) == OPIP:
                p = f.build_point(v, OperationalIntermediatePoint)
                m.operational_intermediate_points.append(p)
            elif type(v) == PP:
                p = f.build_point(v, PassingPoint)
                m.passing_points.append(p)
            elif type(v) == DT:
                p = f.build_point(v, Destination)
                m.destinations.append(p)
            elif type(v) == OPDT:
                p = f.build_point(v, OperationalDestination)
                m.operational_destinations.append(p)
            else:
                raise Exception("Type of point is {}.".format(type(v)))

            m.all_points.append(p)

        first_point = m.all_points[0]
        if first_point.raw_working_arrival_time is not None:
            t = first_point.raw_working_arrival_time
        elif first_point.raw_working_pass_time is not None:
            t = first_point.raw_working_pass_time
        elif first_point.raw_working_departure_time is not None:
            t = first_point.raw_working_departure_time
        else:
            raise Exception()

        tz = timezone_for_date_and_time(m.start_date, t)

        day_incrementor = 0
        o = None
        for p in m.all_points:
            day_incrementor = f.build_times(day_incrementor, o, p, m.start_date, tz)
            o = p

        m._raw = raw
        m._containing_message = containing_message
        m._xml = xml

        return m

    @staticmethod
    def build_point(raw, t):
        r = t()

        r.tiploc = raw.tpl
        r.activity_codes = raw.act
        r.planned_activity_codes = raw.planAct
        r.cancelled = bool(raw.can)
    
        try:
            r.false_tiploc = raw.fd
        except AttributeError:
            r.false_tiploc = None

        try:
            r.route_delay = raw.rdelay
        except:
            r.route_delay = None
        try:     
            r.raw_working_arrival_time = parse(raw.wta).time()
        except AttributeError:
            r.raw_working_arrival_time = None
        try:
            r.raw_working_pass_time = parse(raw.wtp).time()
        except AttributeError:
            r.raw_working_pass_time = None
        try:
            r.raw_working_departure_time = parse(raw.wtd).time()
        except AttributeError:
            r.raw_working_departure_time = None
        try:
            r.raw_public_arrival_time = parse(raw.pta).time()
        except AttributeError:
            r.raw_public_arrival_time = None
        try:
            r.raw_public_departure_time = parse(raw.ptd).time()
        except AttributeError:
            r.raw_public_departure_time = None

        return r
   
    @staticmethod
    def build_times(day_incrementor, last_location, this_location, start_date, tz):

        # Construct all the date/time objects iteratively, checking for back-in-time movement of
        # any of them.
        last_time = None
        if last_location is not None:
            last_time = f.get_last_time(last_location)

        if this_location.raw_working_arrival_time is not None:
            t = this_location.raw_working_arrival_time
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            this_location.working_arrival_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)
        else:
            this_location.working_arrival_time = None

        if this_location.raw_public_arrival_time is not None:
            t = this_location.raw_public_arrival_time
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            this_location.public_arrival_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)
        else:
            this_location.public_arrival_time = None

        if this_location.raw_working_pass_time is not None:
            t = this_location.raw_working_pass_time
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            this_location.working_pass_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)
        else:
            this_location.working_pass_time = None

        if this_location.raw_public_departure_time is not None:
            t = this_location.raw_public_departure_time
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            this_location.public_departure_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)
        else:
            this_location.public_departure_time = None

        if this_location.raw_working_departure_time is not None:
            t = this_location.raw_working_departure_time
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            this_location.working_departure_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)
        else:
            this_location.working_departure_time = None

        # Return the new day_incrementor value.
        return day_incrementor

    @staticmethod
    def get_last_time(l):
        if l.raw_working_departure_time is not None:
            return l.raw_working_departure_time
        elif l.raw_working_pass_time is not None:
            return l.raw_working_pass_time
        elif l.raw_working_arrival_time is not None:
            return l.raw_working_arrival_time
        else:
            raise Exception()


f = ScheduleXMLMessageFactory


