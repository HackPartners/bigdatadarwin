import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models import Schedule, CallingPoint, db
from darwinpush.messagefactories.xml import ScheduleXMLMessageFactory
import darwinpush.xb.pushport as pp

import re

class ScheduleFileLoader:

    def __init__(self, file_location):
        assert(file_location)
        self.file_location = file_location

    def update_daily_schedules(self):

        collect_mode=False
        journey_buffer = []

        for line in open(self.file_location):
            
            if '<Journey' in line:
                assert(not collect_mode)
                collect_mode=True

            elif '</Journey' in line:
                assert(collect_mode)
                
                journey_buffer.append(line)
                journey_string = "".join(journey_buffer)
                journey_string = journey_string.replace("Journey", "schedule")
                journey_string = journey_string.replace("<OR", "<ns2:OR")
                journey_string = journey_string.replace("<PP", "<ns2:PP")
                journey_string = journey_string.replace("<IP", "<ns2:IP")
                journey_string = journey_string.replace("<DT", "<ns2:DT")
                journey_string = journey_string.replace("<OPOR", "<ns2:OPOR")
                journey_string = journey_string.replace("<OPIP", "<ns2:OPIP")
                journey_string = journey_string.replace("<OPDT", "<ns2:OPDT")
                journey_string = journey_string.replace("<OPPP", "<ns2:OPPP")
                journey_string = journey_string.replace("cancelReason", "ns2:cancelReason")
                journey_string = re.sub(r'plat=\"[0-9a-zA-Z\s]+\"', '', journey_string)                
                journey_string = re.sub(r'qtrain=\"[0-9a-zA-Z\s]+\"', '', journey_string)                
                journey_string = re.sub(r'can=\"[0-9a-zA-Z\s]+\"', '', journey_string)     
                journey_string = re.sub(r'act=\"[0-9a-zA-Z\s]+\"', '', journey_string)     

                journey_string = (  '<?xml version="1.0" encoding="UTF-8"?>'
                                    + '<Pport ts="2015-07-20T11:52:07.3487919+01:00" version="12.0" xmlns="http://www.thalesgroup.com/rtti/PushPort/v12" xmlns:ns2="http://www.thalesgroup.com/rtti/PushPort/Schedules/v1">'
                                    + '<uR requestID="0000000000020608" requestSource="at09" updateOrigin="CIS">'
                                    + journey_string
                                    + '</uR>'
                                    + '</Pport>')

                self.add_schedule_from_buffer(journey_string)
                
                journey_buffer = []
                collect_mode=False

            if collect_mode:
                journey_buffer.append(line)

    @db.transaction()
    def add_schedule_from_buffer(self, journey_buffer):
        r = pp.CreateFromDocument(journey_buffer)
        assert(None is r.sR)
        assert(None is not r.uR)
        assert(1 == len(r.uR.schedule))

        m = ScheduleXMLMessageFactory.build(r.uR.schedule[0], r, journey_buffer)

        ###### This code below checks that there are no schedules already stored
        # # We try to find a schedule, and replace it if we do
        # found = (Schedule
        #         .select()
        #         .where(
        #             Schedule.uid == m.uid,
        #             Schedule.rid == m.rid
        #         ))

        # count = found.count()
        # if count > 0:
        #     assert(count == 1)
        #     s = found[0]

        #     # Removing all relevant calling points
        #     CallingPoint.delete().where(
        #         CallingPoint.schedule == s
        #     ).execute()

        # else:
        #     s = Schedule()
        #     s.uid = m.uid
        #     s.rid = m.rid


        # Script assumes new schedules added, and overrides any existing
        s = Schedule()
        s.uid = m.uid
        s.rid = m.rid


        s.headcode = m.headcode
        s.start_date = m.start_date
        s.toc_code = m.toc_code
        s.category = m.category
        s.status = m.status
        s.active = m.active
        s.deleted = m.deleted
        s.cancel_tiploc = m.cancel_reason_tiploc
        s.cancel_code = m.cancel_reason_code
        s.cancel_near = m.cancel_reason_near
        s.save()

        for o in m.all_points:
            p = CallingPoint()
            p.tiploc = o.tiploc
            p.schedule = s
            p.activity_codes = o.planned_activity_codes
            p.cancelled = o.cancelled
            p.false_tiploc = o.false_tiploc
            p.route_delay = o.route_delay
            p.working_arrival = o.raw_working_arrival_time
            p.working_pass = o.raw_working_pass_time
            p.working_departure = o.raw_working_departure_time
            p.public_arrival = o.raw_public_arrival_time
            p.public_departure = o.raw_public_departure_time
            p.type = str(type(o))
            p.save()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You must pass the name of the file as argument")
        exit()
        
    s=ScheduleFileLoader(sys.argv[1])
    s.update_daily_schedules()


