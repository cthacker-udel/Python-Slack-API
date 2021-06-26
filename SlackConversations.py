from SlackClient import SlackClient

class SlackConversations(SlackClient):

    def __init__(self):
        self.channel = None
        self.name = None
        self.is_private = None
        self.team_id = None


    def generate_queries(self):

        body = {}

        if self.channel != None:
            body['channel'] = self.channel
        if self.name != None:
            body['name'] = self.name
        if self.is_private != None:
            body['is_private'] = self.is_private
        if self.team_id != None:
            body['team_id'] = self.team_id

        return body

    def clear_queries(self):
        self.channel = None
        self.name = None
        self.is_private = None
        self.team_id = None