from SlackClient import SlackClient

class SlackAPI(SlackClient):

    def __init__(self):
        self.error = None

    def generate_queries(self):
        body = {}
        if self.error != None:
            body['error'] = self.error
        return body

    def clear_queries(self):
        self.error = None