from darwinpush.messages import *

class Listener:
    def __init__(self, q):
        print("Initialising Listener")
        #self.queue = queue.Queue(maxsize=10000)
        self.queue = q
        #self.process = multiprocessing.Process(target=self._run)
        #self.thread.daemon = True
        #p.start()
        #p.join()
        #self.thread.start()
    
    def _run(self):
        print("Running listener")
        
        while True:
            message = self.queue.get()
            #self.queue.task_done()

            if type(message) == ScheduleMessage:
                self.on_schedule_message(message)
            elif type(message) == DeactivatedMessage:
                self.on_deactivated_message(message)
            elif type(message) == AssociationMessage:
                self.on_association_message(message)
            elif type(message) == TrainStatusMessage:
                self.on_train_status_message(message)
            elif type(message) == StationMessage:
                self.on_station_message(message)
            elif type(message) == TrainAlertMessage:
                self.on_train_alert_message(message)
            elif type(message) == TrainOrderMessage:
                self.on_train_order_message(message)
            elif type(message) == TrackingIdMessage:
                self.on_tracking_id_message(message)
            elif type(message) == AlarmMessage:
                self.on_alarm_message(message)
            else:
                print("Another type of message")

    def on_schedule_message(self, message):
        pass

    def on_deactivated_message(self, message):
        pass

    def on_association_message(self, message):
        pass

    def on_train_status_message(self, message):
        pass

    def on_station_message(self, message):
        pass

    def on_train_alert_message(self, message):
        pass

    def on_train_order_message(self, message):
        pass

    def on_tracking_id_message(self, message):
        pass

    def on_alarm_message(self, message):
        pass


