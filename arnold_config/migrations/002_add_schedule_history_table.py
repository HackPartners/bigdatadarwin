from peewee import *
from .. import database as db
from playhouse.postgres_ext import *

import datetime

class DarwinModel(Model):
    """A base model that will use our Postgres database"""
    class Meta:
        database = db

########################################################################
class ScheduleHistory(DarwinModel):
    uid                 = CharField()
    rid                 = CharField()
    status              = CharField()
    category            = CharField()
    toc_code            = CharField(max_length=3)
    headcode            = CharField()
    cancel_tiploc       = CharField(null=True)
    start_date          = DateField()
    passenget_service   = BooleanField(null=True)
    active              = BooleanField()
    deleted             = BooleanField()
    charter             = BooleanField(null=True)
    cancel_near         = BooleanField(null=True)
    cancel_code         = IntegerField(null=True)
    created             = DateTimeField(default=datetime.datetime.now)

CALLING_POINT_TYPE = (
  ('origin', 'Origin'),
  ('operational_origin', 'Operational Origin'),
  ('intermediate', 'Itermediate Point'),
  ('operational_intermediate', 'Operational Intermediate Point'),
  ('passing', 'Passing Point'),
  ('destination', 'Destination'),
  ('operational_destination', 'Operational Destination'),
)

class CallingPointHistory(DarwinModel):
    schedule            = ForeignKeyField(ScheduleHistory)
    tiploc              = CharField()
    activity_codes      = CharField(null=True)
    false_tiploc        = CharField(null=True)
    route_delay         = CharField(null=True)
    type                = CharField(choices=CALLING_POINT_TYPE)
    cancelled           = BooleanField()
    working_arrival     = TimeField(null=True)
    working_pass        = TimeField(null=True)
    working_departure   = TimeField(null=True)
    public_arrival      = TimeField(null=True)
    public_departure    = TimeField(null=True)
    created             = DateTimeField(default=datetime.datetime.now)

all_tables = [
    ScheduleHistory,
    CallingPointHistory
]

def up():
    db.create_tables(all_tables, safe=True)

def down():
    db.drop_tables(all_tables)

