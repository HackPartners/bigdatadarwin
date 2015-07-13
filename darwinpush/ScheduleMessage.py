class ScheduleMessage:

    def __init__(self, raw):
        self.raw = raw

    """
    The 2-letter TOC code for the train operating company of this service.
    """
    @property
    def toc_code(self):
        return self.raw.toc
        
