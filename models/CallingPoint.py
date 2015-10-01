from peewee import ForeignKeyField, CharField, BooleanField, TimeField, Proxy
from models import DarwinModel

# We define a proxy to avoid circular dependencies with Schedule
ScheduleProxy = Proxy()

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
    schedule            = ForeignKeyField(ScheduleProxy)
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

    class Meta:
        pyxb_mappings = [
            ("tiploc", "tiploc"),
            ("activity_codes", "planned_activity_codes"),
            ("cancelled", "cancelled"),
            ("false_tiploc", "false_tiploc"),
            ("route_delay", "route_delay"),
            ("working_arrival", "raw_working_arrival_time"),
            ("working_pass", "raw_working_pass_time"),
            ("working_departure", "raw_working_departure_time"),
            ("public_departure", "raw_public_departure_time"),
            ("type", "__class__"),
        ]


