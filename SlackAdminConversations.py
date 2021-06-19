from SlackClient import SlackClient

class SlackAdminConversations(SlackClient):

    def __init__(self):
        self.channel_id = None
        self.is_private = None
        self.name = None
        self.description = None
        self.org_wide = None
        self.team_id = None
        self.cursor = None
        self.limit = None
        self.user_ids = []


    def generate_queries(self):

        body = {}

        if self.channel_id != None:
            body['channel_id'] = self.channel_id
        if self.is_private != None:
            body['is_private'] = self.is_private
        if self.name != None:
            body['name'] = self.name
        if self.description != None:
            body['description'] = self.description
        if self.org_wide != None:
            body['org_wide'] = self.org_wide
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        if len(self.user_ids) > 0:
            body['user_ids'] = ','.join(self.user_ids)

        return body

    def clear_queries(self):
        self.channel_id = None
        self.is_private = None
        self.name = None
        self.description = None
        self.org_wide = None
        self.team_id = None
        self.cursor = None
        self.limit = None
        self.user_ids = None