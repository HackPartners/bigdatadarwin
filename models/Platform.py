from peewee import CharField, BooleanField
from models import DarwinModel

class Platform(DarwinModel):
    number              = CharField()
    source              = CharField()
    suppressed          = BooleanField(null=True, default=False)
    suppressed_by_cis   = BooleanField(null=True, default=False)
    confirmed           = BooleanField()

    class Meta:
        pyxb_mapping = [
            ("suppressed", "suppressed"),
            ("suppressed_by_cis", "suppressed_by_cis"),
            ("source", "source"),
            ("confirmed", "confirmed"),
            ("number", "number")
        ]