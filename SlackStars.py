from SlackClient import SlackClient

class SlackStars(SlackClient):

    def __init__(self):

        self.channel = None
        self.file = None
        self.file_comment = None
        self.timestamp = None


    def generate_queries(self):

        body = {}

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

        self.channel = None
        self.file = None
        self.file_comment = None
        self.timestamp = None