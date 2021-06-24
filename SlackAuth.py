from SlackClient import SlackClient

class SlackAuth(SlackClient):

    def __init__(self):
        self.test = None


    def generate_queries(self):
        body = {}

        if self.test != None:
            body['test'] = self.test

        return body

    def clear_queries(self):
        self.test = None