from darwinpush import Client

import os

client = Client(os.environ["STOMP_USER"], os.environ["STOMP_PASS"], os.environ["STOMP_QUEUE"])
client.connect()
client.run()


