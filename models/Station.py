from peewee import TextField, CharField
from playhouse.postgres_ext import ArrayField
from models import DarwinModel

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
