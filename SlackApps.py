from SlackClient import SlackClient

class SlackApps(SlackClient):

    def __init__(self):
        self.event_context = None
        self.cursor= None
        self.limit = None
        self.trigger_id = None
        self.scopes = []

    def generate_queries(self):

        body = {}

        if self.event_context != None:
            body['event_context'] = self.event_context
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        if len(self.scopes) > 0:
            body['scopes'] = ','.join(self.scopes)
        if self.trigger_id != None:
            body['trigger_id'] = self.trigger_id
        return body

    def clear_queries(self):
        self.event_context = None
        self.cursor = None
        self.limit = None
        self.trigger_id = None
        self.scopes = []