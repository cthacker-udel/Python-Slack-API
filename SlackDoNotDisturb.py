from SlackClient import SlackClient

class SlackDoNotDisturb(SlackClient):

    def __init__(self):

        self.team_id = None
        self.user = None


    def generate_queries(self):

        body = {}

        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.user != None:
            body['user'] = self.user
        return body

    def clear_queries(self):

        self.team_id = None
        self.user = None