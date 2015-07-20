from darwinpush.messages.BaseMessage import BaseMessage
from darwinpush.utils import timezone_for_date_and_time
from darwinpush.xb.raw.sch import OR, OPOR, IP, OPIP, PP, DT, OPDT
from darwinpush.xb.raw.ct import DisruptionReasonType

from datetime import datetime, timedelta
from dateutil.parser import *
import pytz

class ScheduleLocation:

    def __init__(self, raw):
        self.raw = raw

    def _build_times(self, day_incrementor, last_location, start_date, tz):
 
        # Construct all the date/time objects iteratively, checking for back-in-time movement of
        # any of them.
        last_time = None
        if last_location is not None:
            last_time = last_location._get_last_time()

        if self.raw_working_arrival_time is not None:
            t = parse(self.raw_working_arrival_time).time()
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            self._working_arrival_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)

        if self.raw_public_arrival_time is not None:
            t = parse(self.raw_public_arrival_time).time()
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            self._public_arrival_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)

        if self.raw_working_pass_time is not None:
            t = parse(self.raw_working_pass_time).time()
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            self._working_pass_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)

        if self.raw_public_departure_time is not None:
            t = parse(self.raw_public_departure_time).time()
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            self._public_departure_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)

        if self.raw_working_departure_time is not None:
            t = parse(self.raw_working_departure_time).time()
            if last_time is not None:
                if last_time > t:
                    day_incrementor += 1
            d = start_date + timedelta(days=day_incrementor)
            self._working_departure_time = tz.localize(datetime.combine(d, t)).astimezone(pytz.utc)

        # Return the new day_incrementor value.
        return day_incrementor

    def _get_first_time(self):
        if self.raw_working_arrival_time is not None:
            return parse(self.raw_working_arrival_time).time()
        elif self.raw_working_pass_time is not None:
            return parse(self.raw_working_pass_time).time()
        elif self.raw_working_departure_time is not None:
            return parse(self.raw_working_departure_time).time()
        else:
            raise Exception()

    def _get_last_time(self):
        if self.working_departure_time is not None:
            return self.working_departure_time.time()
        elif self.working_pass_time is not None:
            return self.working_pass_time.time()
        elif self.working_arrival_time is not None:
            return self.working_arrival_time.time()
        else:
            raise Exception()

    @property
    def tiploc(self):
        return self.raw.tpl

    @property
    def activity_codes(self):
        return self.raw.act

    @property
    def planned_activity_codes(self):
        return self.raw.planAct

    @property
    def cancelled(self):
        return self.raw.can

    @property
    def false_tiploc(self):
        return self.raw.fd

    """
    A delay value that is implied by a change to the service's route. This value has been added to
    the forecast lateness of the service at the previous schedule location when calculating the
    expected lateness of arrival at this location.
    """
    @property
    def route_delay(self):
        try:
            return self.raw.rdelay
        except AttributeError:
            return None

    @property
    def raw_working_arrival_time(self):
        try:
            return self.raw.wta
        except AttributeError:
            return None

    @property
    def raw_public_arrival_time(self):
        try:
            return self.raw.pta
        except AttributeError:
            return None

    @property
    def raw_working_departure_time(self):
        try:
            return self.raw.wtd
        except AttributeError:
            return None

    @property
    def raw_public_departure_time(self):
        try:
            return self.raw.ptd
        except AttributeError:
            return None

    @property
    def raw_working_pass_time(self):
        try:
            return self.raw.wtp
        except AttributeError:
            return None
    
    @property
    def working_arrival_time(self):
        try:
            return self._working_arrival_time
        except AttributeError:
            return None

    @property
    def public_arrival_time(self):
        try:
            return self._public_arrival_time
        except AttributeError:
            return None

    @property
    def working_departure_time(self):
        try:
            return self._working_departure_time
        except AttributeError:
            return None

    @property
    def public_departure_time(self):
        try:
            return self._public_departure_time
        except AttributeError:
            return None

    @property
    def working_pass_time(self):
        try:
            return self._working_pass_time
        except AttributeError:
            return None


class Origin(ScheduleLocation):
    pass


class OperationalOrigin(ScheduleLocation):
    pass


class IntermediatePoint(ScheduleLocation):
    pass


class OperationalIntermediatePoint(ScheduleLocation):
    pass


class PassingPoint(ScheduleLocation):
    pass


class Destination(ScheduleLocation):
    pass


class OperationalDestination(ScheduleLocation):
    pass

class ScheduleMessage(BaseMessage):

    def __init__(self, message):
        super().__init__(message)
        self._build_point_lists()

    def _build_point_lists(self):
        # Loop through all the points in the order they appear in the XML, instantiate the
        # appropriate object for them, and add them to the appropriate list.

        self._origins = []
        self._operational_origins = []
        self._intermediate_points = []
        self._operational_intermediate_points = []
        self._passing_points = []
        self._destinations = []
        self._operational_destinations = []
        self._all_points = []

        for r in self.raw.orderedContent():
            v = r.value
            if type(v) == DisruptionReasonType:
                pass
            elif type(v) == OR:
                p = Origin(v)
                self._origins.append(p)
            elif type(v) == OPOR:
                p = OperationalOrigin(v)
                self._operational_origins.append(p)
            elif type(v) == IP:
                p = IntermediatePoint(v)
                self._intermediate_points.append(p)
            elif type(v) == OPIP:
                p = OperationalIntermediatePoint(v)
                self._operational_intermediate_points.append(p)
            elif type(v) == PP:
                p = PassingPoint(v)
                self._passing_points.append(p)
            elif type(v) == DT:
                p = Destination(v)
                self._destinations.append(p)
            elif type(v) == OPDT:
                p = OperationalDestination(v)
                self._operational_destinations.append(p)
            else:
                raise Exception("Type of point is {}.".format(type(v)))

            self._all_points.append(p)

        first_point = self._all_points[0]
        if first_point.raw_working_arrival_time is not None:
            t = parse(first_point.raw_working_arrival_time).time()
        elif first_point.raw_working_pass_time is not None:
            t = parse(first_point.raw_working_pass_time).time()
        elif first_point.raw_working_departure_time is not None:
            t = parse(first_point.raw_working_departure_time).time()
        else:
            raise Exception()

        tz = timezone_for_date_and_time(self.schedule_start_date, t)

        day_incrementor = 0
        o = None
        for p in self._all_points:
            day_incrementor = p._build_times(day_incrementor, o, self.schedule_start_date, tz)
            o = p

    """
    The train UID.
    """
    @property
    def uid(self):
        return self.raw.uid

    """
    The RTTI unique train ID.
    """
    @property
    def rid(self):
        return self.raw.rid

    """
    The train headcode.
    """
    @property
    def headcode(self):
        return self.raw.trainId

    """
    The schedule start date.
    """
    @property
    def schedule_start_date(self):
        return self.raw.ssd.date()
    
    """
    The 2-letter TOC code for the train operating company of this service.
    """
    @property
    def toc_code(self):
        return self.raw.toc
        
    """
    Boolean indicating whether or not this schedule represents a passenger services.
    """
    @property
    def passenger_service(self):
        return self.raw.isPassengerSvc

    """
    Status of the service, i.e. bus/ferry/train.
    """
    @property
    def status(self):
        return self.raw.status

    """
    Category of the service.
    """
    @property
    def category(self):
        return self.raw.trainCat

    """
    Indicates whether the schedule has been activated in Darwin.
    """
    @property
    def active(self):
        return self.raw.isActive

    """
    Indicates whether the schedule has been deleted in Darwin.
    """
    @property
    def deleted(self):
        return self.raw.deleted

    """
    Indicates whether the schedule is for a charter service.
    """
    @property
    def charter(self):
        return self.raw.isCharter

    """
    ???
    """
    @property
    def cancel_reason(self):
        return self.raw.cancelReason

    """
    Returns a list of the service origins. There can be more than one.
    """
    @property
    def origins(self):
        return self._origins

    """
    Returns a list of the serviec operational origins. There can be more than one.
    """
    @property
    def operational_origins(self):
        return self._operational_origins

    """
    Returns a list of the intermediate locations on the service.
    """
    @property
    def intermediate_points(self):
        return self._intermediate_points

    """
    Returns a list of the operational intermediate locations on the service.
    """
    @property
    def operational_intermediate_points(self):
        return self._operational_intermediate_points

    """
    Returns a list of the passing points on the service.
    """
    @property
    def passing_points(self):
        return self._passing_points

    """
    Returns a list of the service destinations. There can be more than one.
    """
    @property
    def destinations(self):
        return self._destinations

    """
    Returns a list of the operational destinations. There can be more than one.
    """
    @property
    def operational_destinations(self):
        return self._operational_destinations


