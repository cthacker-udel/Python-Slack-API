from SlackClient import SlackClient

class SlackReactions(SlackClient):

    def __init__(self):

        self.channel = None
        self.name = None
        self.timestamp = None

        self.file = None
        self.file_comment = None
        self.full = None


    def generate_queries(self):

        body = {}

        if self.file != None:
            body['file'] = self.file
        if self.file_comment != None:
            body['file_comment'] = self.file_comment
        if self.full != None:
            body['full'] = self.full
        if self.channel != None:
            body['channel'] = self.channel
        if self.name != None:
            body['name'] = self.name
        if self.timestamp != None:
            body['timestamp'] = self.timestamp

        return body


    def clear_queries(self):

        self.file = None
        self.file_comment = None
        self.full = None
        self.channel = None
        self.name = None
        self.timestamp = None