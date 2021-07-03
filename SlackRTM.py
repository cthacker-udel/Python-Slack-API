from SlackClient import SlackClient

class SlackRTM(SlackClient):

    def __init__(self):

        self.batch_presence_aware = None
        self.presence_sub = None

    def generate_queries(self):

        body = {}

        if self.batch_presence_aware != None:
            body['batch_presence_aware'] = self.batch_presence_aware
        if self.presence_sub != None:
            body['presence_sub'] = self.presence_sub
        return body

    def clear_queries(self):

        self.batch_presence_aware = None
        self.presence_sub = None