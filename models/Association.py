from peewee import ForeignKeyField, CharField, BooleanField
from models import DarwinModel, AssociationService

ASSOCIATION_TYPE = (
  ('join', 'Join'),
  ('split', 'Split'),
  ('next', 'Next'),
  ('link', 'Link'),
)

class Association(DarwinModel):
    main_service        = ForeignKeyField(AssociationService, related_name="main_service_set")
    associated_service  = ForeignKeyField(AssociationService, related_name="associated_service_set")
    tiploc              = CharField()
    category            = CharField(choices=ASSOCIATION_TYPE)
    cancelled           = BooleanField(null=True, default=False)
    deleted             = BooleanField()
