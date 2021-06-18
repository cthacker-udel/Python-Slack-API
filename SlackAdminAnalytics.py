from SlackClient import SlackClient

class SlackAdminAnalytics(SlackClient):

    def __init__(self):
        self.type = None
        self.date = None
        self.metadata_only = None


    def generate_queries(self):
        body = {}
        if self.type != None:
            body['type'] = self.type
        if self.date != None:
            body['date'] = self.date
        if self.metadata_only != None:
            body['metadata_only'] = self.metadata_only
        return body