from SlackClient import SlackClient

class SlackTeams(SlackClient):

    def __init__(self):
        self.team_id = None
        self.cursor = None
        self.limit = None
        self.team_domain = None
        self.team_name = None
        self.team_description = None
        self.team_discoverability = None


    def generate_queries(self):
        body = {}
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        if self.team_domain != None:
            body['team_domain'] = self.team_domain
        if self.team_name != None:
            body['team_name'] = self.team_name
        if self.team_description != None:
            body['team_description'] = self.team_description
        if self.team_discoverability != None:
            body['team_discoverability'] = self.team_discoverability
        return body

    def clear_queries(self):
        self.team_id = None
        self.cursor = None
        self.limit = None
        self.team_domain = None
        self.team_name = None
        self.team_description = None
        self.team_discoverability = None