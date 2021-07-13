from SlackClient import SlackClient

class SlackChannels(SlackClient):

    def __init__(self):

        self.channel = None
        self.name = None
        self.team_id = None
        self.validate = None

        self.count = None
        self.inclusive = None
        self.latest = None
        self.oldest = None
        self.unreads = None

        self.include_locale = None


    def generate_queries(self):

        body = {}

        if self.include_locale != None:
            body['include_locale'] = self.include_locale
        if self.channel != None:
            body['channel'] = self.channel
        if self.name != None:
            body['name'] = self.name
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.validate != None:
            body['validate'] = self.validate
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
        self.channel = None
        self.name = None
        self.team_id = None
        self.validate = None
        self.count = None
        self.inclusive = None
        self.latest = None
        self.oldest = None
        self.unreads = None
        self.include_locale = None