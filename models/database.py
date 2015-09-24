"""Database configuration is put in this file so that we can easily import it
from the migrations module and change it for the tests module.

Good part is that we can alter the `db` variable as long as we don't import
other things that connect to the database before that.
"""

import os
from playhouse.db_url import connect
import sys

db_url = os.getenv("DARWINPUSH_DB", None)
if db_url is None:
    print("Cannot start without DARWINPUSH_DB env variable.")
    print("\t export DARWINPUSH_DB=\"postgresql://user:pass@host:5432/name\"")
    sys.exit(1)

# db_user = os.getenv("DARWINPUSH_DBUSER", "hackpartner")
# db_pass = os.getenv("DARWINPUSH_DBPASS", "")
# db_name = os.getenv("DARWINPUSH_DBNAME", "darwin_push_db")

db = connect(db_url)
