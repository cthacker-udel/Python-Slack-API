from SlackClient import SlackClient

class SlackDoNotDisturb(SlackClient):

    def __init__(self):

        self.team_id = None
        self.user = None
        self.users = []


    def generate_queries(self):

        body = {}

        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.user != None:
            body['user'] = self.user
        if len(self.users) > 0:
            body['users'] = self.users
        return body

    def clear_queries(self):

        self.team_id = None
        self.user = None
        self.users = []