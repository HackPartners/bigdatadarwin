from stomp.connect import StompConnection10

import pyxb.utils.domutils as domutils

import darwinpush.xb.pushport as pp

import time
import zlib

class Client:
    def __init__(self, stomp_user, stomp_password, stomp_queue):
        self.stomp_user = stomp_user
        self.stomp_password = stomp_password
        self.stomp_queue = stomp_queue

    def connect(self):
        self._connect()

    def _connect(self):
        self.client = StompClient()
        self.client.connect(self.stomp_user, self.stomp_password, self.stomp_queue, self)

    def _on_message(self, headers, message):
        #print("Message: %s" % headers)
        #print(message.decode("UTF-8"))
        doc = domutils.StringToDOM(message.decode("utf-8"))
        #print(doc.documentElement.tagName)
        try:
            r = pp.CreateFromDOM(doc.documentElement)
            #print(type(r.uR))
            i = r.uR
            if len(i.OW) != 0:
                print("OW type message")
            elif len(i.TS) != 0:
                #print("TS type message")
                pass
            else:
                print("Another message type received")
            #print("Received a Push Port message.")
            m = message.decode("utf-8")
            if "fc" not in m:
                print(m)
        except:
          print("Did not receive a Push Port message.")

    def _on_error(self, headers, message):
        print("Error: %s, %s" % (headers, message))

    def run(self):
        while 1:
           time.sleep(1)


class StompClient:
    def connect(self, user, password, queue, callback_object):
        self.cb = callback_object

        self.conn = StompConnection10([("datafeeds.nationalrail.co.uk", 61613)])
        self.conn.set_listener('', self)
        self.conn.start()
        self.conn.connect(user, password)
        self.conn.subscribe(queue, ack='auto')

    def on_error(self, headers, message):
        self.cb._on_error(headers, message)

    def on_message(self, headers, message):
        decompressed_data = zlib.decompress(message, 16+zlib.MAX_WBITS)
        self.cb._on_message(headers, decompressed_data)


