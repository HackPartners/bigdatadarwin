from peewee import ForeignKeyField, CharField
from models import DarwinModel, LateReason, Forecast, Location, Platform, TrainStatusProxy

class TrainStatus(DarwinModel):
    late_reason         = ForeignKeyField(LateReason, null=True)
    rid                 = CharField()
    uid                 = CharField()
    start               = CharField()
    reverse_formation   = CharField()

    class Meta:
        pyxb_mappings = [
            ("rid", "rid"),
            ("uid", "uid"),
            ("start", "start_date"),
            ("reverse_formation", "reverse_formation"),
        ]

    def fromPyXb(self, message, save=False, recursive=False):
        
        lr = None

        if recursive:
            late_reason = message.late_reason

            if late_reason:
                lr = LateReason()
                lr.fromPyXb(late_reason, save=save, recursive=recursive)

        self.late_reason = lr
        self.rid = message.rid
        self.uid = message.uid
        self.start = message.start_date
        self.reverse_formation = message.reverse_formation

        if save: 
            self.save()


        if recursive:
            for location in message.locations:
                # Building forecasts
                f_arrival = None
                f_departure = None
                f_pass = None

                if location.forecast_arrival_time:
                    f_arrival = Forecast()
                    f_arrival.fromPyXb(location.forecast_arrival_time, save=save, recursive=recursive)

                if location.forecast_departure_time:
                    f_departure = Forecast()
                    f_departure.fromPyXb(location.forecast_departure_time, save=save, recursive=recursive)

                if location.forecast_pass_time:
                    f_pass = Forecast()
                    f_pass.fromPyXb(location.forecast_pass_time, save=save, recursive=recursive)

                # Building platform
                platform = location.platform
                p = None

                if platform:
                    p = Platform()
                    p.source = platform.source
                    p.confirmed = platform.confirmed
                    p.number = platform.number
                    p.fromPyXb(platform, save=save, recursive=recursive)

                # Building location
                l = Location()
                l.train_status = self
                l.platform = p
                l.forecast_arrival = f_arrival
                l.forecast_departure = f_departure
                l.forecast_pass = f_pass
                l.fromPyXb(location, save=save, recursive=recursive)
                l.save()


TrainStatusProxy.initialize(TrainStatus)

