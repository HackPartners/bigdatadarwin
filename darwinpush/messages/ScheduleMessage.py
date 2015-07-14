from darwinpush.messages.BaseMessage import BaseMessage

class ScheduleMessage(BaseMessage):

    """
    The 2-letter TOC code for the train operating company of this service.
    """
    @property
    def toc_code(self):
        return self.raw.toc
        
