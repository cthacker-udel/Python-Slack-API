from SlackClient import SlackClient

class SlackFiles(SlackClient):

    def __init__(self):
        self.file = None
        self.id = None

        self.count = None
        self.cursor = None
        self.limit = None
        self.page = None

    def generate_queries(self):

        body = {}

        if self.file != None:
            body['file'] = self.file
        if self.id != None:
            body['id'] = self.id
        if self.count != None:
            body['count'] = self.count
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        if self.page != None:
            body['page'] = self.page
        return body

    def clear_queries(self):
        self.file = None
        self.id = None
        self.count = None
        self.cursor = None
        self.limit = None
        self.page = None

