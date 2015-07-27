class BaseMessage:

    def __init__(self, raw, containing_message):
        self._raw = raw
        self._containing_message = containing_message

    @property
    def raw(self):
        return self._raw

    @property
    def containing_message(self):
        return self._containing_message


