from SlackClient import SlackClient

class SlackAuth(SlackClient):

    def __init__(self):
        self.test = None
        self.cursor = None
        self.include_icon = None
        self.limit = None


    def generate_queries(self):
        body = {}

        if self.test != None:
            body['test'] = self.test
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.include_icon != None:
            body['include_icon'] = self.include_icon
        if self.limit != None:
            body['limit'] = self.limit

        return body

    def clear_queries(self):
        self.test = None
        self.cursor = None
        self.include_icon = None
        self.limit = None