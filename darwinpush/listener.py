from darwinpush.messages import ScheduleMessage

import queue
import threading

class Listener:
    def __init__(self):
        print("Initialising Listener")
        self.queue = queue.Queue(maxsize=10000)
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()
    
    def _run(self):
        print("Running listener")
        while True:
            message = self.queue.get()
            self.queue.task_done()
            if type(message) == ScheduleMessage:
                self.on_schedule_message(message)
            else:
                print("Another type of message")

