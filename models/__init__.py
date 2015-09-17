from peewee import *
from playhouse.postgres_ext import *

import datetime

db = PostgresqlDatabase('darwin_push_db', user='hackpartner', password='hackpartnerspass')
db.connect()

class DarwinModel(Model):
    """A base model that will use our Postgres database"""
    class Meta:
        database = db

########################################################################
class Schedule(DarwinModel):
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

class CallingPoint(DarwinModel):
    schedule            = ForeignKeyField(Schedule)
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

########################################################################
class Forecast(DarwinModel):
    source              = CharField()
    source_cis          = CharField(null=True)
    actual_removed      = BooleanField()
    unknown_delay       = BooleanField(null=True)
    estimated           = TimeField(null=True)
    working_estimated   = TimeField(null=True)
    actual              = TimeField(null=True)
    lower_limit         = TimeField(null=True)
    created             = DateTimeField(default=datetime.datetime.now)

class Platform(DarwinModel):
    source              = CharField()
    suppressed          = BooleanField(null=True, default=False)
    suppressed_by_cis   = BooleanField(null=True, default=False)
    confirmed           = BooleanField()
    number              = CharField()
    created             = DateTimeField(default=datetime.datetime.now)

class LateReason(DarwinModel):
    code                = CharField()
    tiploc              = CharField(null=True)
    near                = BooleanField()
    created             = DateTimeField(default=datetime.datetime.now)

class TrainStatus(DarwinModel):
    late_reason         = ForeignKeyField(LateReason, null=True)
    rid                 = CharField()
    uid                 = CharField()
    start               = CharField()
    reverse_formation   = CharField()
    created             = DateTimeField(default=datetime.datetime.now)

class Location(DarwinModel):
    train_status        = ForeignKeyField(TrainStatus)
    platform            = ForeignKeyField(Platform, null=True)
    forecast_arrival    = ForeignKeyField(Forecast, related_name="forecast_arrival_set", null=True)
    forecast_departure  = ForeignKeyField(Forecast, related_name="forecast_departure_set", null=True)
    forecast_pass       = ForeignKeyField(Forecast, related_name="forecast_pass_set", null=True)
    tiploc              = CharField()
    suppressed          = BooleanField(null=True, default=False)
    detach_front        = CharField(null=True)
    working_arrival     = TimeField(null=True)
    working_departure   = TimeField(null=True)
    working_pass        = TimeField(null=True)
    public_arrival      = TimeField(null=True)
    public_departure    = TimeField(null=True)
    length              = IntegerField(null=True)
    created             = DateTimeField(default=datetime.datetime.now)

 ########################################################################
class DeactivatedSchedule(DarwinModel):
    rid                 = CharField()
    created             = DateTimeField(default=datetime.datetime.now)

########################################################################
ASSOCIATION_TYPE = (
  ('join', 'Join'),
  ('split', 'Split'),
  ('next', 'Next'),
  ('link', 'Link'),
)

class AssociationService(DarwinModel):
    rid                 = CharField()
    working_arrival     = TimeField(null=True)
    working_departure   = TimeField(null=True)
    working_pass        = TimeField(null=True)
    public_arrival      = TimeField(null=True)
    public_departure    = TimeField(null=True)
    created             = DateTimeField(default=datetime.datetime.now)

class Association(DarwinModel):
    main_service        = ForeignKeyField(AssociationService, related_name="main_service_set")
    associated_service  = ForeignKeyField(AssociationService, related_name="associated_service_set")
    tiploc              = CharField()
    category            = CharField(choices=ASSOCIATION_TYPE)
    cancelled           = BooleanField()
    deleted             = BooleanField()
    created             = DateTimeField(default=datetime.datetime.now)

 ########################################################################
ACTION_TYPE = (
  ('set', 'Set'),
  ('clear', 'Clear'),
)

class TrainOrderItem(DarwinModel):
    rid                 = CharField()   
    headcode            = CharField(null=True) 
    working_arrival     = TimeField(null=True)
    working_departure   = TimeField(null=True)
    working_pass        = TimeField(null=True)
    public_arrival      = TimeField(null=True)
    public_departure    = TimeField(null=True)  
    created             = DateTimeField(default=datetime.datetime.now)

class TrainOrder(DarwinModel):
    action              = CharField(choices=ACTION_TYPE)
    tiploc              = CharField()   
    crs                 = CharField(max_length=3)   
    platform            = CharField()   
    first               = ForeignKeyField(TrainOrderItem, related_name="first_set", null=True)   
    second              = ForeignKeyField(TrainOrderItem, related_name="second_set", null=True)   
    third               = ForeignKeyField(TrainOrderItem, related_name="third_set", null=True) 
    created             = DateTimeField(default=datetime.datetime.now)


 ########################################################################
ALARM_TYPE = (
  ('td_area_fail', 'TD Area Fail'),
  ('td_feed_fail', 'TD Feed Fail'),
  ('tyrell_feed_fail', 'Tyrell Feed Fail'),
)

class Alarm(DarwinModel):
    action              = CharField(choices=ACTION_TYPE)   
    type                = CharField(choices=ALARM_TYPE)   
    aid                 = CharField()   
    created             = DateTimeField(default=datetime.datetime.now)


 ########################################################################
STATION_CATEGORY = (
  ('train', 'Train'),
  ('station', 'Station'),
  ('connection', 'Connection'),
  ('system', 'System'),
  ('misc', 'Misc'),
  ('prior_train', 'Prior Train'),
  ('prior_other', 'Prior Other'),
)

STATION_SEVERITY = (
  ('zero', 'Level Zero'),
  ('one', 'Level One'),
  ('two', 'Level Two'),
  ('three', 'Level Three'),
)

class Station(DarwinModel):
    stations            = ArrayField(CharField)   
    message             = TextField()   
    smid                = CharField()   
    category            = CharField(choices=STATION_CATEGORY)   
    severity            = CharField(choices=STATION_SEVERITY)   
    created             = DateTimeField(default=datetime.datetime.now)

########################################################################
def create_all_tables(safe=True):
    db.create_tables([
            Location,
            TrainStatus,
            LateReason,
            Platform,
            Forecast,
            CallingPoint,
            Schedule,
            DeactivatedSchedule,
            AssociationService,
            Association,
            TrainOrderItem,
            TrainOrder, 
            Station,
            Alarm
        ], safe)
 
 