from SlackClient import SlackClient

class SlackStars(SlackClient):

    def __init__(self):

        self.channel = None
        self.file = None
        self.file_comment = None
        self.timestamp = None

        self.count = None
        self.cursor = None
        self.limit = None
        self.page = None
        self.team_id = None


    def generate_queries(self):

        body = {}

        if self.count != None:
            body['count'] = self.count
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        if self.page != None:
            body['page'] = self.page
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.channel != None:
            body['channel'] = self.channel
        if self.file != None:
            body['file'] = self.file
        if self.file_comment != None:
            body['file_comment'] = self.file_comment
        if self.timestamp != None:
            body['timestamp'] = self.timestamp
        return body


    def clear_queries(self):

        self.count = None
        self.cursor = None
        self.limit = None
        self.page = None
        self.team_id = None
        self.channel = None
        self.file = None
        self.file_comment = None
        self.timestamp = None