from darwinpush.messages import *

from stomp.connect import StompConnection12

import pyxb.utils.domutils as domutils

import darwinpush.xb.pushport as pp

import threading
import sys
import time
import zlib

import logging
log = logging.getLogger("darwinpush")

##### Code for STOMP debugging
#import logging
#console = logging.StreamHandler()
#console.setFormatter(logging.Formatter('[%(asctime)s] %(name)-12s %(levelname)-8s %(message)s'))
#logging.getLogger().addHandler(console)
#logging.getLogger().setLevel(logging.DEBUG)
#LOGGER = logging.getLogger('stomp')
#####

def has_method(_class, _method):
    return callable(getattr(_class, _method, None))

class Client:
    def __init__(self, stomp_user, stomp_password, stomp_queue):
        self.stomp_user = stomp_user
        self.stomp_password = stomp_password
        self.stomp_queue = stomp_queue
        self.listeners = {}

    def connect(self):
        self.connected = True
        self._run()

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def _run(self):
        self.thread = threading.Thread(target=self._connect)
        self.thread.daemon = True
        self.thread.start()

    def _connect(self):
        self.client = StompClient()
        self.client.connect(self.stomp_user, self.stomp_password, self.stomp_queue, self)

        while self.connected:
            time.sleep(1)

    def _on_message(self, headers, message):

        # Decode the message and parse it as an XML DOM.
        doc = domutils.StringToDOM(message.decode("utf-8"))
        
        # Parse the record with pyXb.
        m = pp.CreateFromDOM(doc.documentElement)

        # We aren't ever expecting the Snapshot Record component to contain anything.
        if m.sR is not None:
            print("o.O.o.O Snapshot record is not none.")
            sys.exit(1)

        # We are expecting the Update Record to contain something though!
        if m.uR is None:
            print("o.O.o.O Update record is none.")
            sys.exit(1)
        
        # Make r the record we are looking at.
        r = m.uR

        # Process SCHEDULE messages.
        for i in r.schedule:
            log.debug("SCHEDULE message received.")
            self._emit_processed_message(ScheduleMessage(i, m))

        # Process DEACTIVATED messages.
        for i in r.deactivated:
            log.debug("DEACTIVATED message received.")
            self._emit_processed_message(DeactivatedMessage(i, m))

        # Process ASSOCATION messages.
        for i in r.association:
            log.debug("ASSOCIATION message received.")
            self._emit_processed_message(AssociationMessage(i, m))

        # Process TS messages.
        for i in r.TS:
            log.debug("TS message received.")
            self._emit_processed_message(TrainStatusMessage(i, m))

        # Process OW messages.
        for i in r.OW:
            log.debug("OW message received.")
            self._emit_processed_message(StationMessage(i, m))

        # Process TRAINALERT messages.
        for i in r.trainAlert:
            log.debug("TRAINALERT message received.")
            self._emit_processed_message(TrainAlertMessage(i, m))

        # Process TRAINORDER messages.
        for i in r.trainOrder:
            log.deug("TRAINORDER message received.")
            self._emit_processed_message(TrainOrderMessage(i, m))

        # Process TRACKINGID messages.
        for i in r.trackingID:
            log.debug("TRACKINGID message received.")
            self._emit_processed_message(TrackingIdMessage(i, m))

        # Process ALARM messages.
        for i in r.alarm:
            log.debug("ALARM message received.")
            self._emit_processed_message(AlarmMessage(i, m))

    def _on_error(self, headers, message):
        print("Error: %s, %s" % (headers, message))

    def _emit_processed_message(self, message):
        for name, listener in self.listeners.items():
            listener.queue.put(message)

    def run(self):
        while 1:
           time.sleep(1)


class StompClient:
    def connect(self, user, password, queue, callback_object):
        log.debug("StompClient.connect()")
        
        self.cb = callback_object

        self.conn = StompConnection12([("datafeeds.nationalrail.co.uk", 61613)])
        self.conn.set_listener('', self)
        self.conn.start()
        self.conn.connect(user, password)
        self.conn.subscribe("/queue/"+queue, ack='auto', id='1')

    def on_error(self, headers, message):
        log.debug("StompClient.onError(headers={}, message={})".format(headers, message))
        
        if has_method(self.cb, "_on_error"):
            self.cb._on_error(headers, message)

    def on_connecting(self, host_and_port):
        log.debug("StompClient.onConnecting(host_and_port={})".format(host_and_port))

        if has_method(self.cb, "_on_connecting"):
            self.cb._on_connecting(host_and_port)

    def on_connected(self, headers, body):
        log.debug("StompClient.onConnected(headers={}, body={})".format(headers, body))

        if has_method(self.cb, "_on_connected"):
            self.cb._on_connected(headers, body)

    def on_disconnected(self):
        log.debug("StompClient.onDisconnected()")

        if has_method(self.cb, "_on_disconnected"):
            self.cb._on_disconnected()

    def on_message(self, headers, message):
        log.debug("StompClient.onMessage(headers={}, body=<truncated>)".format(headers))

        if has_method(self.cb, "_on_message"):
            try:
                decompressed_data = zlib.decompress(message, 16+zlib.MAX_WBITS)
                try:
                    self.cb._on_message(headers, decompressed_data)
                except Exception as e:
                    log.exception("Exception occurred parsing DARWIN message: {}.".format(decompressed_data))
            except Exception as e:
                log.exception("Exception occurred decompressing the STOMP message.")


