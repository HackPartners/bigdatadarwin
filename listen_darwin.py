#!/usr/bin/env python3

from darwinpush import Client, Listener
from darwinpush.messages.AssociationMessage import AssociationCategory
from models import *

import os
import queue
import time

class MyListener(Listener):
    def __init__(self, q, quit):
        print("Setting Up")
        super().__init__(q, quit)

    @db.transaction()
    def on_schedule_message(self, m):
        print("Schedule message: ", m.uid, m.rid, m.start_date)

        # We try to find a schedule, and replace it if we do
        found = (Schedule
                .select()
                .where(
                    Schedule.uid == m.uid,
                    Schedule.rid == m.rid
                ))

        count = found.count()
        if count > 0:
            assert(count == 1)
            s = found[0]

            print("Removing calling points")

            # Removing all relevant calling points
            CallingPoint.delete().where(
                CallingPoint.schedule == s
            ).execute()

        else:
            s = Schedule()
        
        s.fromPyXb(m, save=True, recursive=True)

    @db.transaction()
    def on_deactivated_message(self, message):
        print("^^^^^^^^^^^^ DEACTIVATED!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        d = DeactivatedSchedule()
        d.rid = message.rid
        d.save()

    @db.transaction()
    def on_association_message(self, message):
        print("^^^^^^^^^^^^ ASSOCIATION!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        main_svc = build_assoc_svc(message.main_service)
        assoc_svc = build_assoc_svc(message.associated_service)

        main_svc.save()
        assoc_svc.save()

        a = Association()
        a.main_service = main_svc
        a.associated_service = assoc_svc
        a.tiploc = message.tiploc
        a.category = message.category
        a.deleted = message.deleted
        a.save()

    @db.transaction()
    def on_alarm_message(self, message):
        print("^^^^^^^^^^^^ ALARM!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        a = Alarm()
        a.action = message.alarm_action
        a.type = message.alarm_type
        a.aid = a.aid
        a.save()

    def on_station_message(self, message):
        print("^^^^^^^^^^^^ STATION!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        s = Station()
        s.stations = message.stations
        s.message = str(message.message)
        s.smid = message.smid
        # TODO: Change to actual category and severity types
        s.category = str(message.category)
        s.severity = str(message.severity)
        s.save()

    @db.transaction()
    def on_tracking_id_message(self, message):
        print("^^^^^^^^^^^^ TRACKING ID!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    @db.transaction()
    def on_train_alert_message(self, message):
        print("^^^^^^^^^^^^ ALERT!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    @db.transaction()
    def on_train_order_message(self, message):
        print("^^^^^^^^^^^^ TRAIN ORDER!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        first = None
        second = None
        third = None

        if message.first:
            first = build_train_order_item(message.first)
            first.save()

        if message.second:
            second = build_train_order_item(message.second)
            second.save()

        if message.third:
            third = build_train_order_item(message.third)
            third.save()


        t = TrainOrder()
        t.first = first
        t.second = second
        t.third = third
        # TODO: Change action to be set/clear
        t.action = message.action
        t.tiploc = message.tiploc
        t.crs = message.crs
        t.platform = message.platform
        t.save()

    @db.transaction()
    def on_train_status_message(self, message):
        print("^^^^^^^^^^^^ NEW TRAIN STATUS MESSAGE!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        t = TrainStatus()
        t.fromPyXb(message, save=True, recursive=True)

def build_assoc_svc(assoc_svc):
    a = AssociationService()
    a.rid = assoc_svc.rid
    a.working_arrival = assoc_svc.working_arrival_time
    a.working_departure = assoc_svc.working_departure_time
    a.working_pass = assoc_svc.working_pass_time
    a.public_arrival = assoc_svc.public_arrival_time
    a.public_departure = assoc_svc.public_departure_time
    return a

def build_forecast(forecast):
    f = Forecast()
    f.source = forecast.source
    f.source_cis = forecast.source_cis
    f.estimated = forecast.estimated_time
    f.working_estimated = forecast.working_estimated_time
    f.actual = forecast.actual_time
    f.actual_removed = forecast.actual_time_removed
    f.manual_estimated = forecast.manual_estimate_lower_limit_minutes
    f.manual_delay = forecast.manual_estimate_unknown_delay
    return f

def build_train_order_item(train_order):
    to = TrainOrderItem()
    to.rid = train_order.rid
    to.headcode = train_order.headcode
    to.working_arrival = train_order.working_arrival_time
    to.working_departure = train_order.working_departure_time
    to.working_pass = train_order.working_pass_time
    to.public_arrival = train_order.public_arrival_time
    to.public_departure = train_order.public_departure_time
    return to

# Make this file importable for debugging

if __name__ == "__main__":

    # Instantiate the Push Port client.
    client = Client(os.environ["STOMP_USER"],
                    os.environ["STOMP_PASS"],
                    os.environ["STOMP_QUEUE"],
                    MyListener)

    # Disable default reconnection attempts of Client
    client.auto_retry = False

    # Connect the Push Port client.
    client.connect()

    print("Connected")
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("Disconnecting client...")
        client.disconnect()
        print("Bye")
