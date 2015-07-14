from darwinpush import Client, Listener

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
        print(message.toc_code)

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


