from darwinpush.messages import *
from darwinpush.messagefactories.xml import *

import logging
log = logging.getLogger("darwinpush")

class Parser:
    def __init__(self, q_in, q_out):
        self.q_in = q_in
        self.q_out = q_out

    def run(self):
        while True:
            (m, message) = self.q_in.get()
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
                o = ScheduleMessage(i, m, message)
                self.q_out.put(o)

            # Process DEACTIVATED messages.
            for i in r.deactivated:
                log.debug("DEACTIVATED message received.")
                o = DeactivatedMessage(i, m, message)
                self.q_out.put(o)

            # Process ASSOCATION messages.
            for i in r.association:
                log.debug("ASSOCIATION message received.")
                AssociationMessage(i, m, message)
                self.q_out.put(o)

            # Process TS messages.
            for i in r.TS:
                log.debug("TS message received.")
                o = TrainStatusXMLMessageFactory.build(i, m, message)
                self.q_out.put(o)

            # Process OW messages.
            for i in r.OW:
                log.debug("OW message received.")
                o = StationMessage(i, m, message)
                self.q_out.put(o)

            # Process TRAINALERT messages.
            for i in r.trainAlert:
                log.debug("TRAINALERT message received.")
                TrainAlertMessage(i, m, message)
                self.q_out.put(o)

            # Process TRAINORDER messages.
            for i in r.trainOrder:
                log.deug("TRAINORDER message received.")
                TrainOrderMessage(i, m, message)
                self.q_out.put(o)

            # Process TRACKINGID messages.
            for i in r.trackingID:
                log.debug("TRACKINGID message received.")
                o = TrackingIdMessage(i, m, message)
                self.q_out.put(o)

            # Process ALARM messages.
            for i in r.alarm:
                log.debug("ALARM message received.")
                o = AlarmMessage(i, m, message)
                self.q_out.put(o)


