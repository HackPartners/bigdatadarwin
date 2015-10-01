from peewee import Model, DateTimeField

import datetime

from models.database import db
db.connect()

ACTION_TYPE = (
  ('set', 'Set'),
  ('clear', 'Clear'),
)

ALARM_TYPE = (
  ('td_area_fail', 'TD Area Fail'),
  ('td_feed_fail', 'TD Feed Fail'),
  ('tyrell_feed_fail', 'Tyrell Feed Fail'),
)

class DarwinModel(Model):
    """A base model that will use our Postgres database"""
    created = DateTimeField(default=datetime.datetime.now)

    def fromPyXb(self, message, save=False, recursive=False):
        """Function that takes an equivalent PyXb darwin object and converts it into a Peewee model.

        Args:
            message (PyXb Object): The PyXb equivallent object to the model.
            save (Boolean): If true, the model will be saved to the database automatically.
            recursive (Boolean): If true, all foreign key fields will be recursed.
        """
        fm = self._meta.pyxb_mappings

        for (field, mapping) in fm:
            # Iterating throuhg all the mappings and replacing the values
            self.__setattr__(
                field, 
                message.__getattribute__(mapping))

        if save:
            self.save()

    class Meta:
        database = db
        pyxb_mappings = []

