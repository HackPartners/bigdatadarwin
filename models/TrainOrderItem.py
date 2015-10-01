from peewee import CharField, TimeField
from models import DarwinModel

class TrainOrderItem(DarwinModel):
    rid                 = CharField()
    headcode            = CharField(null=True)
    working_arrival     = TimeField(null=True)
    working_departure   = TimeField(null=True)
    working_pass        = TimeField(null=True)
    public_arrival      = TimeField(null=True)
    public_departure    = TimeField(null=True)

    class Meta:
        pyxb_mappings = [
            ("rid", "rid"),
            ("headcode", "headcode"),
            ("working_arrival", "working_arrival_time"),
            ("working_departure", "working_departure_time"),
            ("working_pass", "working_pass_time"),
            ("public_arrival", "public_arrival_time"),
            ("public_departure", "public_departure_time")
        ]