from darwinpush import Client, Listener
from darwinpush.messages.AssociationMessage import AssociationCategory

import os
import queue
import time

# Create a listener to process the messages.
class MyListener(Listener):
    def __init__(self):
        # TODO: Do any setup you need to do here.
        print("Setting Up")

        # Finally, call the Super Class initialiser.
        super().__init__()

    def on_schedule_message(self, message):
        #for OR in message.origins:
        #    print(OR.tiploc)
        #for OR in message.operational_origins:
        #    print(OR.public_arrival_time)
        #print("---------------")
        pass

    def on_deactivated_message(self, message):
        #print(message.rid)
        pass

    def on_association_message(self, message):
        if message.category is not AssociationCategory.Next:
            print(message.category)

    def on_alarm_message(self, message):
        print("Alarm Message Type: {}".format(type(message.raw)))
        print(message.raw.toxml())
        print("=========================================================")

    def on_station_message(self, message):
        print("Station Message Type: {}".format(type(message.raw)))
        print(message.raw.toxml())
        print("=========================================================")

    def on_tracking_id_message(self, message):
        print("Tracking ID Message Type: {}.".format(type(message.raw)))
        print(message.raw.toxml())
        print("=========================================================")

    def on_train_alert_message(self, message):
        print("Train Alert Message Type: {}.".format(type(message.raw)))
        print(message.raw.toxml())
        print("=========================================================")

    def on_train_order_message(self, message):
        print("Train Order Message Type: {}.".format(type(message.raw)))
        print(message.raw.toxml())
        print("=========================================================")

    def on_train_status_message(self, message):
        #print("Train Status Message Type: {}.".format(type(message.raw)))
        if message.late_reason is not None:
            if message.late_reason.tiploc is not None and bool(message.late_reason.near) is not False:
                print("{} -- {}".format(message.late_reason.tiploc, message.late_reason.near))
                print(message.raw.toxml())
                print("====================================================")
        pass


# Instantiate the Push Port client.
client = Client(os.environ["STOMP_USER"], os.environ["STOMP_PASS"], os.environ["STOMP_QUEUE"])

# Instantiate our listener class and register it with the Push Port client.
listener = MyListener()
client.register_listener('', listener)

# Connect the Push Port client.
client.connect()

# Keep the main thread running indefinitely while we receive messages.
while True:
    time.sleep(1)


