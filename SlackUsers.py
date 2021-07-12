from SlackClient import SlackClient

class SlackUsers(SlackClient):

    def __init__(self):

        self.cursor = None
        self.exclude_archived = None
        self.limit = None
        self.team_id = None
        self.types = None
        self.user = None
        self.include_locale = None
        self.email = None
        self.presence = None


    def generate_queries(self):

        body = {}

        if self.presence != None:
            body['presence'] = self.presence
        if self.email != None:
            body['email'] = self.email
        if self.include_locale != None:
            body['include_locale'] = self.include_locale
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.exclude_archived != None:
            body['exclude_archived'] = self.exclude_archived
        if self.limit != None:
            body['limit'] = self.limit
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.types != None:
            body['types'] = self.types
        if self.user != None:
            body['user'] = self.user
        return body

    def clear_queries(self):

        self.include_locale = None
        self.cursor = None
        self.exclude_archived = None
        self.limit = None
        self.team_id = None
        self.types = None
        self.user = None
        self.email = None
        self.presence = None
