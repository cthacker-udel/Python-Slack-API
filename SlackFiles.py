from SlackClient import SlackClient

class SlackFiles(SlackClient):

    def __init__(self):
        self.file = None
        self.id = None

    def generate_queries(self):

        body = {}

        if self.file != None:
            body['file'] = self.file
        if self.id != None:
            body['id'] = self.id
        return body

    def clear_queries(self):
        self.file = None
        self.id = None

