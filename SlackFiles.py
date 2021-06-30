from SlackClient import SlackClient

class SlackFiles(SlackClient):

    def __init__(self):
        self.file = None
        self.id = None

        self.count = None
        self.cursor = None
        self.limit = None
        self.page = None

        self.channel = None
        self.show_files_hidden_by_limit = None
        self.ts_from = None
        self.ts_to = None
        self.types = None
        self.user = None

    def generate_queries(self):

        body = {}

        if self.channel != None:
            body['channel'] = self.channel
        if self.show_files_hidden_by_limit != None:
            body['show_files_hidden_by_limit'] = self.show_files_hidden_by_limit
        if self.ts_from != None:
            body['ts_from'] = self.ts_from
        if self.ts_to != None:
            body['ts_to'] = self.ts_to
        if self.types != None:
            body['types'] = self.types
        if self.user != None:
            body['user'] = self.user
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
        self.channel = None
        self.show_files_hidden_by_limit = None
        self.ts_from = None
        self.ts_to = None
        self.types = None
        self.user = None

