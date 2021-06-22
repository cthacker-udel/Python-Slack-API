from SlackClient import SlackClient

class SlackTeams(SlackClient):

    def __init__(self):
        self.team_id = None
        self.cursor = None
        self.limit = None


    def generate_queries(self):
        body = {}
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        return body

    def clear_queries(self):
        self.team_id = None
        self.cursor = None
        self.limit = None