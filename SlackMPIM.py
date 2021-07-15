from SlackClient import SlackClient

class SlackMPIM(SlackClient):

    def __init__(self):
        self.channel = None
        self.count = None
        self.inclusive = None
        self.latest = None
        self.oldest = None
        self.unreads = None
        self.cursor = None
        self.limit = None
        self.ts = None
        self.users = []


    def generate_queries(self):

        body = {}


        if len(self.users) > 0:
            body['users'] = ','.join(self.users)
        if self.ts != None:
            body['ts'] = self.ts
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        if self.channel != None:
            body['channel'] = self.channel
        if self.count != None:
            body['count'] = self.count
        if self.inclusive != None:
            body['inclusive'] = self.inclusive
        if self.latest != None:
            body['latest'] = self.latest
        if self.oldest != None:
            body['oldest'] = self.oldest
        if self.unreads != None:
            body['unreads'] = self.unreads
        return body


    def clear_queries(self):
        self.ts = None
        self.limit = None
        self.cursor = None
        self.channel = None
        self.count = None
        self.inclusive = None
        self.latest = None
        self.oldest = None
        self.unreads = None
        self.users = []