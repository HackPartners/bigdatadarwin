from stomp.connect import StompConnection12

import pyxb.utils.domutils as domutils

import darwinpush.xb.pushport as pp

from darwinpush.parser import Parser

import enum
import multiprocessing
import sys
import threading
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

def listener_process(c, q):
    listener = c(q)
    listener._run()


def parser_process(q_in, q_out):
    parser = Parser(q_in, q_out)
    parser.run()


class ErrorType(enum.Enum):

    DecompressionError = 1
    ParseError = 2


class Error:
    def __init__(self, error_type, message, exception):
        self._error_type = error_type
        self._payload = payload
        self._exception = exception

    @property
    def payload(self):
        return self._payload

    @property
    def error_type(self):
        return self._error_type

    @property
    def exception(self):
        return self._exception

    def __str__(self):
        return str(self._exception)

    def __repr__(self):
        return str(self)


def has_method(_class, _method):
    return callable(getattr(_class, _method, None))

class Client:
    """ The object that acts as the Client to the National Rail enquries Darwin Push Port STOMP server.

    You should instantiate an instance of this object, with the required parameters to act as the
    client to the Darwin Push Port. Listeners registered with this object will be passed messages
    that are received from the server once they have been turned into the relevant python object.

    Args:
        stomp_user: Your STOMP user name taken from the National Rail Open Data portal.
        stomp_password: Your STOMP password taken from the National Rail Open Data portal.
        stomp_queue: Your STOMP queue name taken from the National Rail Open Data portal.
        listener: The class object (not an instance of it) for your Listener subclass. 

    """

    def __init__(self, stomp_user, stomp_password, stomp_queue, listener):
        self.stomp_user = stomp_user
        self.stomp_password = stomp_password
        self.stomp_queue = stomp_queue

        self.listener_queue = multiprocessing.Queue()
        self.parser_queue = multiprocessing.Queue()
        self.listener_process = multiprocessing.Process(target=listener_process, args=(listener, self.listener_queue))
        self.listener_process.start()
        self.parser_process = multiprocessing.Process(target=parser_process, args=(self.parser_queue, self.listener_queue))
        self.parser_process.start()

    def connect(self):
        """ Connect to the Darwin Push Port and start receiving messages."""
        self.connected = True
        self._run()

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

        self.parser_queue.put((m, message))

    def _on_error(self, headers, message):
        print("Error: %s, %s" % (headers, message))

    def _on_local_error(self, error):
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ Caught Message Error in Client Thread +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(str(error))
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-")

    def run(self):
        while 1:
           time.sleep(1)


class StompClient:
    def connect(self, user, password, queue, callback_object):
        log.debug("StompClient.connect()")
        
        self.cb = callback_object

        self.conn = StompConnection12([("datafeeds.nationalrail.co.uk", 61613)], auto_decode=False)
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

    def on_local_error(self, error):
        if has_method(self.cb, "_on_local_error"):
            self.cb._on_local_error(error)

    def on_message(self, headers, message):
        log.debug("StompClient.onMessage(headers={}, body=<truncated>)".format(headers))

        if has_method(self.cb, "_on_message"):
            try:
                decompressed_data = zlib.decompress(message, 16+zlib.MAX_WBITS)
                try:
                    self.cb._on_message(headers, decompressed_data)
                except Exception as e:
                    log.exception("Exception occurred parsing DARWIN message: {}.".format(decompressed_data))
                    self.on_local_error(Error(ErrorType.ParseError, decompressed_data, e))
            except Exception as e:
                log.exception("Exception occurred decompressing the STOMP message.")
                self.on_local_error(Error(ErrorType.DecompressionError, (headers, message), e))


