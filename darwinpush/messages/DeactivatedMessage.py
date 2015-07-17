from darwinpush.messages.BaseMessage import BaseMessage

class DeactivatedMessage(BaseMessage):
    
    """
    The RTTI unique train ID.
    """
    @property
    def rid(self):
        return self.raw.rid


