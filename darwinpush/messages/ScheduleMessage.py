from darwinpush.messages.BaseMessage import BaseMessage
from darwinpush.utils import timezone_for_date_and_time
from darwinpush.xb.raw.sch import OR, OPOR, IP, OPIP, PP, DT, OPDT
from darwinpush.xb.raw.ct import DisruptionReasonType

from datetime import datetime, timedelta
from dateutil.parser import *
import pytz

class Location:

    """
    Attributes
    ----------
    route_delay : int
        A delay value that is implied by a change to the service's route. This value has been added
        to the forecast lateness of the service at the previous schedule location when calculating
        the expected lateness of arrival at this location.
    """

    pass

class Origin(Location):
    pass


class OperationalOrigin(Location):
    pass


class IntermediatePoint(Location):
    pass


class OperationalIntermediatePoint(Location):
    pass


class PassingPoint(Location):
    pass


class Destination(Location):
    pass


class OperationalDestination(Location):
    pass

class ScheduleMessage:
    """ Represents a ScheduleMessage.

    Attributes
    ----------
    uid : string
        The Network Rail Schedule UID.
    rid : string
        The Darwin Push Port RTTI identifier for this schedule. This is the unique identifier for
        Schedules in the Push Port data.
    headcode : string
        The headcode, or trainID.
    start_date : date
        The date on which this schedule starts.
    toc_code : string
        The two-letter Train Operating Company code for this service.
    passenger_service : bool
        True indicates this is a passenger service, otherwise False.
    status : string
        The "Status" of the service, ie. bus/ferry/train.
    category : string
        The "category" of the service.
    active : bool
        True if the schedule has been activated in Darwin, otherwise False.
    deleted : bool
        True indicates the service has been deleted in Darwin, and thus should not be shown to end
        users. This is different from *cancelled* where the service should still be shown to users
        but indicated as cancelled, whereas a *deleted* service should never be shown at all.
    charter : bool
        True indicates that this schedule message describes a charter train. N.b. not all charter
        trains are present in the Darwin Push Port feed, but those that are will have this
        property set to True.
    cancel_reason : int
        The cancelleation reason code if the service has been cancelled.
    origins : List of Origin
        An ordered list of the Origins this service has.
    operational_origins : List of OperationalOrigin
        An ordered list of the Operational Origins this service has.
    intermediate_points : List of IntermediatePoint
        An ordered list of the Intermediate Points this service has.
    operational_intermediate_points : List of OperationalIntermediatePoint
        An ordered list of the Operational Intermediate Points this service has.
    passing_points : List of PassingPoint
        An ordered list of the Passing Points this service has.
    destinations : List of Destination
        An ordered list of the Destinations this service has.
    operational_destinations : List of OperationalDestination
        An ordered list of the Operational Destinations this service has.

    """

    pass


