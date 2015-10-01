from peewee import CharField, ForeignKeyField, DateTimeField
from models import DarwinModel, TrainOrderItem, ACTION_TYPE

class TrainOrder(DarwinModel):
    action              = CharField(choices=ACTION_TYPE)
    tiploc              = CharField()
    crs                 = CharField(max_length=3)
    platform            = CharField()
    first               = ForeignKeyField(TrainOrderItem, related_name="first_set", null=True)
    second              = ForeignKeyField(TrainOrderItem, related_name="second_set", null=True)
    third               = ForeignKeyField(TrainOrderItem, related_name="third_set", null=True)

    class Meta:
        pyxb_mappings = [
            ("action", "action"),
            ("tiploc", "tiploc"),
            ("crs", "crs"),
            ("platform", "platform"),
        ]