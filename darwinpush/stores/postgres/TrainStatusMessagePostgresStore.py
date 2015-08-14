from darwinpush.stores.postgres.BasePostgresStore import BasePostgresStore
from darwinpush.stores.postgres.ScheduleMessagePostgresStore import ScheduleMessagePostgresStore

from collections import OrderedDict

class TrainStatusMessagePostgresStore(BasePostgresStore):
    
    def __init__(self, connection):
        super().__init__(connection)
        s = ScheduleMessagePostgresStore

        self.update_schedule_query = "UPDATE {} SET {} WHERE {}".format(
                s.table_schedule_name,
                ", ".join(["{}=%s".format(k) for k, v in list(s.table_schedule_fields.items())[14:]]),
                "rid=%s")

        self.select_location_query = "SELECT {} from {} WHERE {}".format(
                "id, route_delay, working_arrival_time, public_arrival_time, working_pass_time, public_departure_time, working_departure_time",
                s.table_schedule_location_name,
                " and ".join(["{} IS NOT DISTINCT FROM %s".format(k) for k in [
                    "rid",
                    "tiploc",
                    "raw_working_arrival_time",
                    #"raw_public_arrival_time",
                    "raw_working_pass_time",
                    #"raw_public_departure_time",
                    "raw_working_departure_time"
                ]]))

    def create_tables(self):
        # No tables to create - the ScheduleMessagePostgresStore is responsible for that.
        pass

    def save_train_status_message(self, message):
        # Check the train concerned is in the database.
        cursor = self.connection.cursor()

        cursor.execute("SELECT rid FROM schedule WHERE rid=%s", (message.rid,))
        
        if cursor.rowcount != 1:
            print("--- Cannot apply because we don't have the relevant schedule record yet.")
            pass
        else:
            print("+++ Schedule record is present. Can apply.")
            if message.late_reason is None:
                late_reason_code = None
                late_reason_tiploc = None
                late_reason_near = None
            else:
                late_reason_code = message.late_reason.code
                late_reason_tiploc = message.late_reason.tiploc
                late_reason_near = message.late_reason.near

            cursor.execute(self.update_schedule_query, (
                message.reverse_formation,
                late_reason_code,
                late_reason_tiploc,
                late_reason_near,
                message.rid
            ))

            for l in message.locations:
                cursor.execute(self.select_location_query, (
                    message.rid,
                    l.tiploc,
                    l.working_arrival_time,
                    #l.public_arrival_time,
                    l.working_pass_time,
                    #l.public_departure_time,
                    l.working_departure_time,
                ))
                if cursor.rowcount == 0:
                    print("   --- 0 Matching Schedule locations found.")
                    pass
                elif cursor.rowcount == 1:
                    #print("   +++ 1 Matching Schedule location found.")
                    pass
                else:
                    print("   !!! {} matching schedule locations found.".format(cursor.rowcount))
                    pass

        self.connection.commit()
        cursor.close()


