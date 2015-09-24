This will be a short guide on how to setup the listener.

## Environment variables

All the configuration is done using environment variables.

Currently, the following are in use (with the default values):

    export STOMP_USER="" # no default
    export STOMP_PASS="" # no default
    export STOMP_QUEUE="" # no default

    export DARWINPUSH_DBHOST="localhost" 
    export DARWINPUSH_DBUSER="hackpartner"
    export DARWINPUSH_DBPASS=""
    export DARWINPUSH_DBNAME="darwin_push_db"

    #  These are made to default to the values set
    # for the production environment at the moment:
    export TEST_DARWINPUSH_DBHOST=""
    export TEST_DARWINPUSH_DBUSER=""
    export TEST_DARWINPUSH_DBPASS=""
    export TEST_DARWINPUSH_DBNAME=""

## Migrations

We use peewee for our ORM and arnold for managing migrations. We
have in plan to change it to a more automatic solution but until
then, to run the migrations:

    arnold up 0


## Install requirements

The usual way:

    pip install -r requirements.txt
