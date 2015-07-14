class BaseMessage:

    def __init__(self, raw):
        self._raw = raw

    @property
    def raw(self):
        return self._raw
