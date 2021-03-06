from SlackClient import SlackClient

class SlackConversations(SlackClient):

    def __init__(self):
        self.channel = None
        self.name = None
        self.is_private = None
        self.team_id = None
        self.cursor = None
        self.inclusive = None
        self.latest = None
        self.limit = None
        self.oldest = None
        self.include_locate = None
        self.include_non_members = None
        self.users = None
        self.user = None
        self.exclude_archived = None
        self.types = None
        self.ts = None
        self.purpose = None
        self.topic = None


    def generate_queries(self):

        body = {}
        if self.topic != None:
            body['topic'] = self.topic
        if self.purpose != None:
            body['purpose'] = self.purpose
        if self.ts != None:
            body['ts'] = self.ts
        if self.exclude_archived != None:
            body['exclude_archived'] = self.exclude_archived
        if self.types != None:
            body['types'] = self.types
        if self.user != None:
            body['user'] = self.user
        if self.users != None:
            body['users'] = self.users
        if self.include_locate:
            body['include_locale'] = self.include_locate
        if self.include_non_members != None:
            body['include_num_members']
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.inclusive != None:
            body['inclusive'] = self.inclusive
        if self.latest != None:
            body['latest'] = self.latest
        if self.limit != None:
            body['limit'] = self.limit
        if self.oldest != None:
            body['oldest'] = self.oldest
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
        self.cursor = None
        self.inclusive = None
        self.latest = None
        self.limit = None
        self.oldest = None
        self.exclude_archived = None
        self.types = None
        self.user = None
        self.users = None
        self.ts = None
        self.purpose = None
        self.topic = None