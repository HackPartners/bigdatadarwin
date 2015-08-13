from darwinpush.messages.BaseMessage import BaseMessage

from dateutil.parser import *

import enum

class UnknownAssociationCategoryError(Exception):
    pass


class AssociationCategory(enum.Enum):
    
    Join = 1
    Split = 2
    Next = 3
    Link = 4

    @staticmethod
    def from_string(s):
        if s == 'JJ':
            return AssociationCategory.Join
        if s == 'VV':
            return AssociationCategory.Split
        if s == 'NP':
            return AssociationCategory.Next
        if s == 'LK':
            return AssociationCategory.Link

        raise UnknownAssociationCategoryError("Unknown AssociationCategory '{}' received in Association Message.".format(s))


class AssociationService:
    
    def __init__(self, raw):
        self.raw = raw
        
        try:
            self._working_arrival_time = parse(self.raw.wta).time()
        except AttributeError:
            self._working_arrival_time = None

        try:
            self._working_departure_time = parse(self.raw.wtd).time()
        except AttributeError:
            self._working_departure_time = None

        try:
            self._working_pass_time = parse(self.raw.wtp).time()
        except AttributeError:
            self._working_pass_time = None

        try:
            self._public_arrival_time = parse(self.raw.pta).time()
        except AttributeError:
            self._public_arrival_time = None
        
        try:
            self._public_departure_time = parse(self.raw.ptd).time()
        except AttributeError:
            self._public_departure_time = None

    @property
    def rid(self):
        return self.raw.rid

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


class AssociationMessage(BaseMessage):
    """ Message representing an Association of some form between two Schedules.

    More information about the underlying Push Port message can be found at the NROD Wiki
    `Association Data <http://nrodwiki.rockshore.net/index.php/Darwin:Association_Element>`_
    page.
    """

    @property
    def main_service(self):
        return AssociationService(self.raw.main)

    @property
    def associated_service(self):
        return AssociationService(self.raw.assoc)

    @property
    def tiploc(self):
        return self.raw.tiploc

    @property
    def category(self):
        return AssociationCategory.from_string(self.raw.category)

    @property
    def cancelled(self):
        return bool(self.raw.isCancelled)

    @property
    def deleted(self):
        return bool(self.raw.isDeleted)


