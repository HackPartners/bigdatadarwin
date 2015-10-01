from peewee import CharField
from models import DarwinModel

class DeactivatedSchedule(DarwinModel):
    rid                 = CharField()
