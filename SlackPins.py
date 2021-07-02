from SlackClient import SlackClient

class SlackPins(SlackClient):

    def __init__(self):
        self.timestamp = None
        self.channel = None

    def generate_queries(self):

        body = {}

        if self.channel != None:
            body['channel'] = self.channel
        if self.timestamp != None:
            body['timestamp'] = self.timestamp

        return body

    def clear_queries(self):

        self.timestamp = None
        self.channel = None