from SlackClient import SlackClient

class SlackOAuth(SlackClient):

    def __init__(self):
        self.code = None
        self.redirect_uri = None
        self.single_channel = None


    def generate_queries(self):

        body = {}

        if self.code != None:
            body['code'] = self.code
        if self.redirect_uri != None:
            body['redirect_uri'] = self.redirect_uri
        if self.single_channel != None:
            body['single_channel'] = self.single_channel

        return body

    def clear_queries(self):

        self.code = None
        self.redirect_uri = None
        self.single_channel = None