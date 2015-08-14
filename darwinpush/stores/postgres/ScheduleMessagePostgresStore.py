from darwinpush.messages.ScheduleMessage import Origin, OperationalOrigin, IntermediatePoint, OperationalIntermediatePoint, PassingPoint, Destination, OperationalDestination
from darwinpush.stores.postgres.BasePostgresStore import BasePostgresStore

from collections import OrderedDict

class ScheduleMessagePostgresStore(BasePostgresStore):

    table_schedule_name = "schedule"
    table_schedule_fields = OrderedDict([
            ("rid", "varchar PRIMARY KEY NOT NULL"),
            ("uid", "varchar NOT NULL"),
            ("headcode", "varchar NOT NULL"),
            ("start_date", "date NOT NULL"),
            ("toc_code", "varchar"),
            ("passenger_service", "boolean"),
            ("status", "varchar"),
            ("category", "varchar"),
            ("active", "boolean"),
            ("deleted", "boolean"),
            ("charter", "boolean"),
            ("cancel_reason_code", "integer"),
            ("cancel_tiploc", "varchar"),
            ("cancel_reason_near", "boolean")
    ])
    
    table_schedule_location_name = "schedule_location"
    table_schedule_location_fields = OrderedDict([
            ("id", "bigserial PRIMARY KEY NOT NULL"),
            ("rid", "varchar REFERENCES schedule (rid)"),
            ("type", "smallint NOT NULL"),
            ("position", "smallint NOT NULL"),
            ("tiploc", "varchar NOT NULL"),
            ("activity_codes", "varchar"),
            ("planned_activity_codes", "varchar"),
            ("cancelled", "boolean"),
            ("false_tiploc", "varchar"),
            ("route_delay", "integer"),
            ("working_arrival_time", "timestamp with time zone"),
            ("public_arrival_time", "timestamp with time zone"),
            ("working_pass_time", "timestamp with time zone"),
            ("public_departure_time", "timestamp with time zone"),
            ("working_departure_time", "timestamp with time zone"),
    ])

    def __init__(self, connection):
        super().__init__(connection)

        self.insert_schedule_query = "INSERT into {} ({}) VALUES({})".format(
                self.table_schedule_name,
                ", ".join(["{}".format(k) for k, v in self.table_schedule_fields.items()]),
                ", ".join(["%s" for n in range(0, len(self.table_schedule_fields))]))
        
        self.insert_schedule_location_query = "INSERT into {} ({}) VALUES({})".format(
                self.table_schedule_location_name,
                ", ".join(["{}".format(k) for k, v in list(self.table_schedule_location_fields.items())[1:]]),
                ", ".join(["%s" for n in range(1, len(self.table_schedule_location_fields))]))

        self.update_schedule_query = "UPDATE {} SET {} WHERE {}".format(
                self.table_schedule_name,
                ", ".join(["{}=%s".format(k) for k, v in list(self.table_schedule_fields.items())[1:]]),
                "rid=%s")

    def create_tables(self):
        cursor = self.connection.cursor()
        
        schedule_query = "CREATE TABLE IF NOT EXISTS {} ({});".format(self.table_schedule_name,
                ", ".join(["{} {}".format(k, v) for k, v in self.table_schedule_fields.items()]))
        
        schedule_locations_query = "CREATE TABLE IF NOT EXISTS {} ({});".format(self.table_schedule_location_name,
                ", ".join(["{} {}".format(k, v) for k, v in self.table_schedule_location_fields.items()]))

        cursor.execute(schedule_query)
        cursor.execute(schedule_locations_query)
        
        self.connection.commit()
        
        cursor.close()

    def save_schedule_message(self, message):
        # Check if the schedule message is already found with that RTTI ID
        cursor = self.connection.cursor()

        cursor.execute("SELECT rid FROM schedule WHERE rid=%s", (message.rid,));
        print(cursor.rowcount)

        # Check if this is a new Schedule.
        if cursor.rowcount == 0:
            cursor.execute(self.insert_schedule_query, (
                message.rid,
                message.uid,
                message.headcode,
                message.start_date,
                message.toc_code,
                message.passenger_service,
                message.status,
                message.category,
                message.active,
                message.deleted,
                message.charter,
                message.cancel_reason_code,
                message.cancel_reason_tiploc,
                message.cancel_reason_near
            ))
        else:
           cursor.execute(self.update_schedule_query, (
                message.uid,
                message.headcode,
                message.start_date,
                message.toc_code,
                message.passenger_service,
                message.status,
                message.category,
                message.active,
                message.deleted,
                message.charter,
                message.cancel_reason_code,
                message.cancel_reason_tiploc,
                message.cancel_reason_near,
                message.rid
            ))
           cursor.execute("DELETE from {} WHERE rid=%s".format(self.table_schedule_location_name), (message.rid,));
        i = 0
        for p in message.all_points:
            cursor.execute(self.insert_schedule_location_query, (
                message.rid,
                self.point_type(p),
                i,
                p.tiploc,
                p.activity_codes,
                p.planned_activity_codes,
                p.cancelled,
                p.false_tiploc,
                p.route_delay,
                p.working_arrival_time,
                p.public_departure_time,
                p.working_pass_time,
                p.public_departure_time,
                p.working_departure_time
            ))
            i += 1
        
        self.connection.commit()

    def point_type(self, p):
        if type(p) == Origin:
            return 1
        if type(p) == OperationalOrigin:
            return 2
        if type(p) ==IntermediatePoint:
            return 3
        if type(p) == OperationalIntermediatePoint:
            return 4
        if type(p) == PassingPoint:
            return 5
        if type(p) == Destination:
            return 6
        if type(p) == OperationalDestination:
            return 7


