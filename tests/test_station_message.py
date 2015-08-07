import os
import sys
sys.path.append(os.getcwd())

import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messages import StationMessage
from darwinpush.messages.StationMessage import StationMessageCategory, StationMessageSeverity

class TestStationMessage:

    def get_station_message_from_file(self, file_path):
        with open(file_path) as f:
            r = pp.CreateFromDocument(f.read())
            assert(r.sR is None)
            assert(r.uR is not None)
            assert(len(r.uR.OW) == 1)

            s = StationMessage(r.uR.OW[0], r)
            return s

    def test_station_message(self):
        m = self.get_station_message_from_file("tests/data/station_message.xml")
        assert(None is not m)

        assert(1 == len(m.stations))
        assert("BSK" == m.stations[0])
        assert(51504 == m.smid)
        assert(StationMessageCategory.Station == m.category)
        assert(StationMessageSeverity.LevelOne == m.severity)
        
        assert("The lifts on platforms 2 and 3 at Basingstoke will be out of use until at least September 2015. " == str(m.message))

    def test_station_message_many_stations(self):
        m = self.get_station_message_from_file("tests/data/station_message__many_stations_train.xml")
        assert(None is not m)

        assert(10 == len(m.stations))
        assert("RNR" == m.stations[0])
        assert("WRT" == m.stations[1])
        assert("SAH" == m.stations[2])
        assert("WRN" == m.stations[3])
        assert("SHM" == m.stations[4])
        assert("CMR" == m.stations[5])
        assert("NWA" == m.stations[6])
        assert("HXM" == m.stations[7])
        assert("GNT" == m.stations[8])
        assert("NRW" == m.stations[9])
        assert(52096 == m.smid)
        assert(StationMessageCategory.Train == m.category)
        assert(StationMessageSeverity.LevelOne == m.severity)

    def test_station_message_link(self):
        m = self.get_station_message_from_file("tests/data/station_message__link.xml")
        assert(None is not m)

        assert(2 == len(m.stations))
        assert("ISP" == m.stations[0])
        assert("BIT" == m.stations[1])
        assert(44534 == m.smid)
        assert(StationMessageCategory.Station == m.category)
        assert(StationMessageSeverity.LevelZero == m.severity)
        
        assert("Because of engineering work, there are no train services at this station until 26 October 2015. Rail replacement buses leave Bicester Village from the main bus stop at Pringle Drive. More details are available from the Current Engineering Work area of the <a href=\"http://nationalrail.co.uk/service_disruptions/62816.aspx\">National Rail Enquiries website</a>. " == str(m.message))

    def test_station_message_paragraph(self):
        m = self.get_station_message_from_file("tests/data/station_message__paragraph.xml")
        assert(None is not m)

        assert(5 == len(m.stations))
        assert("HKC" == m.stations[0])
        assert("HTF" == m.stations[1])
        assert("KID" == m.stations[2])
        assert("SED" == m.stations[3])
        assert("SMA" == m.stations[4])
        assert(52087 == m.smid)
        assert(StationMessageCategory.Station == m.category)
        assert(StationMessageSeverity.LevelZero == m.severity)
        assert("<p>The ticket office at this station is currently closed. </p>" == str(m.message))

    def test_station_message_multiple_paragraphs_and_link(self):
        m = self.get_station_message_from_file("tests/data/station_message__multiple_paragraphs_and_link.xml")
        assert(None is not m)

        assert(0 == len(m.stations))
        assert(52169 == m.smid)
        assert(StationMessageCategory.Train == m.category)
        assert(StationMessageSeverity.LevelOne == m.severity)
        assert("<p>Journeys between Ipswich and Cambridge are being delayed by up to 10 minutes. More details can be found in <a href=\"http://nationalrail.co.uk/service_disruptions/104721.aspx\">Latest Travel News.</a></p><p></p><p></p>" == str(m.message))


