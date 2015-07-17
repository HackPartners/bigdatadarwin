from darwinpush.messages.BaseMessage import BaseMessage

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
            return AssociationCateogry.Link

        raise UnknownAssociationCategoryError("Unknown AssociationCategory '{}' received in Association Message.".format(s))


class AssociationService:
    
    def __init__(self, raw):
        self.raw = raw

    @property
    def rid(self):
        return self.raw.rid

    @property
    def working_arrival_time(self):
        return self.raw.wta

    @property
    def working_departure_time(self):
        return self.raw.wtd

    @property
    def working_pass_time(self):
        return self.raw.wtp

    @property
    def public_arrival_time(self):
        return self.raw.pta

    @property
    def public_departure_time(self):
        return self.raw.ptd


class AssociationMessage(BaseMessage):

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
        return self.raw.isCancelled

    @property
    def deleted(self):
        return self.raw.isDeleted


