from SlackClient import SlackClient

class SlackUserGroups(SlackClient):

    def __init__(self):

        self.channels = None
        self.name = None
        self.description = None
        self.handle = None
        self.include_count = None
        self.team_id = None

        self.usergroup = None

    def generate_queries(self):

        body = {}

        if self.usergroup != None:
            body['usergroup'] = self.usergroup
        if self.channels != None:
            body['channels'] = self.channels
        if self.name != None:
            body['name'] = self.name
        if self.description != None:
            body['description'] = self.description
        if self.handle != None:
            body['handle'] = self.handle
        if self.include_count != None:
            body['include_count'] = self.include_count
        if self.team_id != None:
            body['team_id'] = self.team_id
        return body

    def clear_queries(self):

        self.channels = None
        self.name = None
        self.description = None
        self.handle = None
        self.include_count = None
        self.team_id = None
        self.usergroup = None
