from darwinpush.messages.BaseMessage import BaseMessage

class ScheduleLocation:

    def __init__(self, raw):
        self.raw = raw

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
    def working_arrival_time(self):
        try:
            return self.raw.wta
        except AttributeError:
            return None

    @property
    def public_arrival_time(self):
        try:
            return self.raw.pta
        except AttributeError:
            return None

    @property
    def working_departure_time(self):
        try:
            return self.raw.wtd
        except AttributeError:
            return None

    @property
    def public_departure_time(self):
        try:
            return self.raw.ptd
        except AttributeError:
            return None

    @property
    def working_pass_time(self):
        try:
            return self.raw.wtp
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
        self.point_lists_built = False

    def _build_point_lists(self):
        # Loop through all the points in the order they appear in the XML, instantiate the
        # appropriate object for them, and add them to the appropriate list.a

        self._origins = []
        self._operational_origins = []
        self._intermediate_points = []
        self._operational_intermediate_points = []
        self.passing_points = []
        self.destinations = []
        self.operational_destinations = []
        self.all_calling_points = []


        day_incrementer = 0
        for r in self.raw.orderedContent():
            
        
        self.point_lists_built = True


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
        return [Origin(OR) for OR in self.raw.OR]

    """
    Returns a list of the serviec operational origins. There can be more than one.
    """
    @property
    def operational_origins(self):
        return [OperationalOrigin(OPOR) for OPOR in self.raw.OPOR]

    """
    Returns a list of the intermediate locations on the service.
    """
    @property
    def intermediate_points(self):
        return [IntermediatePoint(IP) for IP in self.raw.IP]

    """
    Returns a list of the operational intermediate locations on the service.
    """
    @property
    def operational_intermediate_points(self):
        return [OperationalIntermediatePoint(OPIP) for OPIP in self.raw.OPIP]

    """
    Returns a list of the passing points on the service.
    """
    @property
    def passing_points(self):
        return [PassingPoint(PP) for PP in self.raw.PP]

    """
    Returns a list of the service destinations. There can be more than one.
    """
    @property
    def destinations(self):
        return [Destination(DT) for DT in self.raw.DT]

    """
    Returns a list of the operational destinations. There can be more than one.
    """
    @property
    def operational_destinations(self):
        return [OperationalDestination(OPDT) for OPDT in self.raw.OPDT]


