"""Database configuration is put in this file so that we can easily import it
from the migrations module and change it for the tests module.

Good part is that we can alter the `db` variable as long as we don't import
other things that connect to the database before that.
"""

from peewee import PostgresqlDatabase
import os

db_user = os.getenv("DARWINPUSH_DBUSER", "hackpartner")
db_pass = os.getenv("DARWINPUSH_DBPASS", "")
db_name = os.getenv("DARWINPUSH_DBNAME", "darwin_push_db")

db = PostgresqlDatabase(db_name, user=db_user, password=db_name)
