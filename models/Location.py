from peewee import CharField, ForeignKeyField, BooleanField, TimeField, IntegerField, Proxy
from models import DarwinModel, Forecast, Platform

TrainStatusProxy = Proxy()

class Location(DarwinModel):
    train_status        = ForeignKeyField(TrainStatusProxy)
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

    class Meta:
        pyxb_mappings = [
            ("tiploc", "tiploc"),
            ("suppressed", "suppressed"),
            ("detach_front", "detach_front"),
            ("working_arrival", "working_arrival_time"),
            ("working_departure", "working_departure_time"),
            ("working_pass", "working_pass_time"),
            ("public_arrival", "public_arrival_time"),
            ("public_departure", "public_departure_time"),
            ("length", "length"),
        ]

        