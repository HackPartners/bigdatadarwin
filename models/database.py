"""Database configuration is put in this file so that we can easily import it
from the migrations module and change it for the tests module.

Good part is that we can alter the `db` variable as long as we don't import
other things that connect to the database before that.
"""

import os
from playhouse.db_url import connect
import sys

db_user = os.getenv("DARWINPUSH_DBUSER", "hackpartner")
db_pass = os.getenv("DARWINPUSH_DBPASS", "password")
db_name = os.getenv("DARWINPUSH_DBNAME", "darwin_push_db")
db_host = os.getenv("DARWINPUSH_DBHOST", "localhost")
db_port = os.getenv("DARWINPUSH_DBPORT", "5432")

db_url = ("postgresql" + "://" + db_user + ":" + db_pass + "@" + db_host + ":" + db_port + "/" + db_name)

db = connect(db_url)
