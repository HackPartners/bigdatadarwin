from peewee import CharField, DateField, BooleanField, IntegerField
from models import DarwinModel, CallingPoint, ScheduleProxy

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

    def fromPyXb(self, message, save=False, recursive=False):
        
        super(Schedule, self).fromPyXb(message, save=save, recursive=recursive)

        if recursive:
            for o in message.all_points:
                p = CallingPoint()
                p.schedule = self
                p.fromPyXb(o, save=save, recursive=recursive)

    class Meta:
        pyxb_mappings = [
            ("uid", "uid"),
            ("rid", "rid"),
            ("headcode", "headcode"),
            ("start_date", "start_date"),
            ("toc_code", "toc_code"),
            ("category", "category"),
            ("status", "status"),
            ("active", "active"),
            ("deleted", "deleted"),
            ("cancel_tiploc", "cancel_reason_tiploc"),
            ("cancel_code", "cancel_reason_code"),
            ("cancel_near", "cancel_reason_near"),
            ("start_date", "start_date"),
            ("start_date", "start_date"),
            ("start_date", "start_date")
        ]

# We now initialize the schedule (walkaroudn for circular dependency)
ScheduleProxy.initialize(Schedule)

