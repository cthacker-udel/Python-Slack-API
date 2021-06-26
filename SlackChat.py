from SlackClient import SlackClient

class SlackChat(SlackClient):

    def __init__(self):
        self.channel = None
        self.ts = None
        self.as_user = None

    def generate_queries(self):

        body = {}

        if self.channel != None:
            body['channel'] = self.channel
        if self.ts != None:
            body['ts'] = self.ts
        if self.as_user != None:
            body['as_user'] = self.as_user
        return body


    def clear_queries(self):
        self.channel = None
        self.ts = None
        self.as_user = None
