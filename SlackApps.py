from SlackClient import SlackClient

class SlackApps(SlackClient):

    def __init__(self):
        self.event_context = None
        self.cursor= None
        self.limit = None