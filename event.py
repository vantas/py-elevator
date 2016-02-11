class Event:
    def __init__(self, eventType, Time):
        self.eventType = eventType
        self.eventTime = eventTime
        self.client = None
        self.elevator = None
        self.floor = None
