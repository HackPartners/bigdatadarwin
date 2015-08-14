from darwinpush import Client, Listener
from darwinpush.stores.postgres import PostgresConnection, ScheduleMessagePostgresStore

import os
import time

class PostgresListener(Listener):
    def __init__(self, queue):
        super().__init__(queue)
        
        self.connection = PostgresConnection(host=os.environ["POSTGRES_HOST"],
                                             dbname=os.environ["POSTGRES_DB"],
                                             user=os.environ["POSTGRES_USER"],
                                             password=os.environ["POSTGRES_PASS"])
        self.connection.connect()

        self.schedule_store = ScheduleMessagePostgresStore(self.connection)

    def on_schedule_message(self, message):
        print("SCHEDULE MESSAGE")
        self.schedule_store.save_schedule_message(message)


connection = PostgresConnection(host=os.environ["POSTGRES_HOST"],
                                dbname=os.environ["POSTGRES_DB"],
                                user=os.environ["POSTGRES_USER"],
                                password=os.environ["POSTGRES_PASS"])
connection.connect()
sm = ScheduleMessagePostgresStore(connection)
sm.create_tables()

client = Client(os.environ["STOMP_USER"],
                os.environ["STOMP_PASS"],
                os.environ["STOMP_QUEUE"],
                PostgresListener)

client.connect()

while True:
    time.sleep(1)


