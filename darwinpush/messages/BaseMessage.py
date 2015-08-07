class BaseMessage:

    def __init__(self, raw, containing_message, xml):
        self._raw = raw
        self._containing_message = containing_message
        self._xml = xml

    @property
    def raw(self):
        return self._raw

    @property
    def containing_message(self):
        return self._containing_message

    @property
    def xml(self):
        return self._xml


