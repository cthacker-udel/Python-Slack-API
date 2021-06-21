from SlackClient import SlackClient

class SlackAdminEmoji(SlackClient):

    def __init__(self):
        self.name = None
        self.url = None


    def generate_queries(self):

        body = {}

        if self.name != None:
            body['name'] = self.name
        if self.url != None:
            body['url'] = self.url
        return body

    def clear_queries(self):

        self.name = None
        self.url = None