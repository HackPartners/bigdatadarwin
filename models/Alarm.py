from peewee import CharField
from models import DarwinModel, ACTION_TYPE, ALARM_TYPE

class Alarm(DarwinModel):
    action              = CharField(choices=ACTION_TYPE)
    type                = CharField(choices=ALARM_TYPE)
    aid                 = CharField(null=True)
