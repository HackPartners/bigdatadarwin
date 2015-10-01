from peewee import CharField, BooleanField, TimeField
from models import DarwinModel

class Forecast(DarwinModel):
    source              = CharField()
    source_cis          = CharField(null=True)
    actual_removed      = BooleanField()
    unknown_delay       = BooleanField(null=True)
    estimated           = TimeField(null=True)
    working_estimated   = TimeField(null=True)
    actual              = TimeField(null=True)
    lower_limit         = TimeField(null=True)

    class Meta:
        pyxb_mappings = [
            ("source", "source"),
            ("source_cis", "source_cis"),
            ("estimated", "estimated_time"),
            ("working_estimated", "working_estimated_time"),
            ("actual", "actual_time"),
            ("actual_removed", "actual_time_removed"),
            ("manual_estimated", "manual_estimate_lower_limit_minutes"),
            ("manual_delay", "manual_estimate_unknown_delay"),
        ]