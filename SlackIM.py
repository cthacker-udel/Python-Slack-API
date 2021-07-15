from SlackClient import SlackClient

class SlackIM(SlackClient):

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
        self.user = None
        self.include_locale = None
        self.return_im = None

    def generate_queries(self):

        body = {}

        if self.user != None:
            body['user'] = self.user
        if self.include_locale != None:
            body['include_locale'] = self.include_locale
        if self.return_im != None:
            body['return_im'] = self.return_im
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
        self.user = None
        self.include_locale = None
        self.return_im = None
        self.ts = None
        self.cursor = None
        self.limit = None
        self.channel = None
        self.count = None
        self.inclusive = None
        self.latest = None
        self.oldest = None
        self.unreads = None