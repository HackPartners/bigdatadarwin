from peewee import CharField, TimeField
from models import DarwinModel

class AssociationService(DarwinModel):
    rid                 = CharField()
    working_arrival     = TimeField(null=True)
    working_departure   = TimeField(null=True)
    working_pass        = TimeField(null=True)
    public_arrival      = TimeField(null=True)
    public_departure    = TimeField(null=True)
