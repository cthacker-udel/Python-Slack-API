from SlackClient import SlackClient

class SlackChannels(SlackClient):

    def __init__(self):

        self.channel = None
        self.name = None
        self.team_id = None
        self.validate = None


    def generate_queries(self):

        body = {}

        if self.channel != None:
            body['channel'] = self.channel
        if self.name != None:
            body['name'] = self.name
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.validate != None:
            body['validate'] = self.validate
        return body


    def clear_queries(self):
        self.channel = None
        self.name = None
        self.team_id = None
        self.validate = None