from darwinpush.messages.BaseMessage import BaseMessage

class LateReason:

    def __init__(self, raw):
        self.raw = raw

    @property
    def tiploc(self):
        return self.raw.tiploc

    @property
    def near(self):
        return self.raw.near


class TrainStatusMessage(BaseMessage):
    
    @property
    def late_reason(self):
        return self.raw.LateReason




