from darwinpush import Client, Listener
from darwinpush.messages.AssociationMessage import AssociationCategory

import os
import queue
import time

# Create a listener to process the messages.
class MyListener(Listener):
    def __init__(self, q):
        # TODO: Do any setup you need to do here.
        print("Setting Up")
        self.counter = 0
        self.ts_counter = 0

        # Finally, call the Super Class initialiser.
        super().__init__(q)

    def on_schedule_message(self, message):
        #if message.passenger_service is False:
        #    print("^^^^^^^^^^^^ Passenger Service: False ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        #    print(message._xml)
        if (hasattr(message, "cancel_reason")
                and message.cancel_reason is not None):
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& CANCEL REASON NOT NONE &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print(message.cancel_reason)
            print(message._xml)
        if message.active is False:
            print("^^^^^^^^^^^^ Active: False ^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print(message._xml)
        #if message.cancel_reason is not None:
        #    print("^^^^^^^^^^^^ Cancel Reason not null ^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        #    print(message._xml)
        if message.charter is True:
            print("^^^^^^^^^^^^^^ Charter ^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print(message._xml)
        #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        
        #print(message._xml)
        #for OR in message.origins:
        #    print(OR.tiploc)
        #for OR in message.operational_origins:
        #    print(OR.public_arrival_time)
        #print("---------------")
        pass

    def on_deactivated_message(self, message):
        self.counter += 1
        if self.counter % 100 == 0:
            print("100 Deactivated Messages")
        pass

    def on_association_message(self, message):
        if message.category == AssociationCategory.Next or message.category == AssociationCategory.Join or message.category == AssociationCategory.Split:
            return
        print("***************** Assoc Message: {} *********************************".format(message.category))
        print(message._xml)
        print("**********************************************************************************************")
        #if message.category is not AssociationCategory.Next:
        #    print(message.category)

    def on_alarm_message(self, message):
        print("===================================== BEGIN: Alarm =================================")
        print(message._xml)
        print("===================================== END: Alarm =================================")

    def on_station_message(self, message):
        #print("===================================== BEGIN: Station =================================")
        #print(message._xml)
        #print("===================================== END: Station =================================")
        pass

    def on_tracking_id_message(self, message):
        print("===================================== BEGIN: Tracking ID =================================")
        print(message._xml)
        print("===================================== END: Tracking ID =================================")

    def on_train_alert_message(self, message):
        print("===================================== BEGIN: Alert =================================")
        print(message._xml)
        print("===================================== END: Alert =================================")

    def on_train_order_message(self, message):
        print("===================================== BEGIN: Train Order =================================")
        print(message._xml)
        print("===================================== END: Train Order =================================")

    def on_train_status_message(self, message):
        #print("Train Status Message Type: {}.".format(type(message.raw)))
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #print(message._xml.decode("utf-8"))
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")a
        #self.ts_counter += 1
        #if self.ts_counter % 1000 == 0:
        #    print("1000 forecasts received")
        if message.late_reason is not None:
            #print(message.locations)
            # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            # print(message._xml.decode("utf-8"))
            # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if message.late_reason.tiploc is not None:
                #print("!£$%^&*()!£$%^&*(!£$%^&*()£$%^&*()$%^&*()£$%^&*()£$%^&*()")
                #print("{} -- {}".format(message.late_reason.tiploc, message.late_reason.near))
                #print(message._xml)
                #print("====================================================")
                pass
        pass


# Instantiate the Push Port client.
client = Client(os.environ["STOMP_USER"], os.environ["STOMP_PASS"], os.environ["STOMP_QUEUE"], MyListener)

# Connect the Push Port client.
client.connect()

# Keep the main thread running indefinitely while we receive messages.
while True:
    time.sleep(1)


