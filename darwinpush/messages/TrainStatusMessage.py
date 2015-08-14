class LateReason:
    """ Represents the reason for the late running of a service.

    Attributes
    ----------
    code : int
        The reason code for the late running of the service.
    tiploc : string
        The location to which this late running reason corresponds.
    near : bool
        True if the TIPLOC property should be interpreted as "near" instead of "at", otherwise
        False. e.g. "Signal Failure near Plymouth" instead of "Signal Failure at Plymouth"
    """
    
    def __repr__(self):
        return "LateReason({},{},{})".format(self.code, self.tiploc, self.near)

    def __str__(self):
        return __repr__()


class Location:
    pass

class Forecast:
    pass

class Platform:
    pass

class TrainStatusMessage:
    """ Represents a Train Status Message from the Push Port.
    
    Attributes
    ----------
    late_reason : LateReason
        The reason for why the service is late.
    locations : list of Locations 
        The locations for which information is present in this message.
    rid : string
        The Darwin RTTI identifier of the schedule this message applies to. This should be
        considered to be the unique identifier of the corresponding schedule message.
    uid : string
        The Network Rail UID of the schedule this message applies to.
    start_date : date
        The start date of the schedule this message applies to.
    reverse_formation : bool
        True if the train is operating in the reverse of it's normal formation, otherwise False.
    """


