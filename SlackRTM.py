from SlackClient import SlackClient

class SlackRTM(SlackClient):

    def __init__(self):

        self.batch_presence_aware = None
        self.presence_sub = None

        self.include_locale = None
        self.mpim_aware = None
        self.no_latest = None
        self.no_unreads = None
        self.simple_latest = None


    def generate_queries(self):

        body = {}
        if self.include_locale != None:
            body['include_locale'] = self.include_locale
        if self.mpim_aware != None:
            body['mpim_aware'] = self.mpim_aware
        if self.no_latest != None:
            body['no_latest'] = self.no_latest
        if self.no_unreads != None:
            body['no_unreads'] = self.no_unreads
        if self.simple_latest != None:
            body['simple_latest'] = self.simple_latest
        if self.batch_presence_aware != None:
            body['batch_presence_aware'] = self.batch_presence_aware
        if self.presence_sub != None:
            body['presence_sub'] = self.presence_sub
        return body

    def clear_queries(self):

        self.batch_presence_aware = None
        self.presence_sub = None
        self.include_locale = None
        self.mpim_aware = None
        self.no_latest = None
        self.no_unreads = None
        self.simple_latest = None