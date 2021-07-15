from SlackClient import SlackClient

class SlackMPIM(SlackClient):

    def __init__(self):
        self.channel = None


    def generate_queries(self):

        body = {}

        if self.channel != None:
            body['channel'] = self.channel


    def clear_queries(self):
        self.channel = None