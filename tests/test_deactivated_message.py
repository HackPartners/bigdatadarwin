import os
import sys
sys.path.append(os.getcwd())

import pytest

import darwinpush.xb.pushport as pp
from darwinpush.messages import DeactivatedMessage

class TestDeactivatedMessage:

    def get_deactivated_message_from_file(self, file_path):
        with open(file_path) as f:
            r = pp.CreateFromDocument(f.read())
            assert(r.sR is None)
            assert(r.uR is not None)
            assert(len(r.uR.deactivated) == 1)

            s = DeactivatedMessage(r.uR.deactivated[0], r)
            return s

    def test_deactivated_message(self):
        m = self.get_deactivated_message_from_file("tests/data/deactivated_message.xml")
        assert(None is not m)

        assert("201508063391581" == m.rid)


