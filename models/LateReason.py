from peewee import CharField, BooleanField
from models import DarwinModel

class LateReason(DarwinModel):
    code                = CharField()
    tiploc              = CharField(null=True)
    near                = BooleanField()

    class Meta:
        pyxb_mappings = [
            ("code", "code"),
            ("tiploc", "tiploc"),
            ("near", "near")
        ]