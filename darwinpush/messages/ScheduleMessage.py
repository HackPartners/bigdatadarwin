from darwinpush.messages.BaseMessage import BaseMessage

class ScheduleMessage(BaseMessage):

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
        return self.raw.ssd
    
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


