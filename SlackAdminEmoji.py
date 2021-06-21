from SlackClient import SlackClient

class SlackAdminEmoji(SlackClient):

    def __init__(self):
        self.name = None
        self.url = None
        self.alias_for = None
        self.cursor = None
        self.limit = None


    def generate_queries(self):

        body = {}

        if self.name != None:
            body['name'] = self.name
        if self.url != None:
            body['url'] = self.url
        if self.alias_for != None:
            body['alias_for'] = self.alias_for
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        return body

    def clear_queries(self):

        self.name = None
        self.url = None
        self.alias_for = None
        self.cursor = None
        self.limit = None