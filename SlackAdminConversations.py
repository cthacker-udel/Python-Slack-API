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
        self.cursor = None
        self.limit = None
        self.query = None
        self.search_channel_types = None
        self.sort = None
        self.sort_dir = None
        self.team_ids = None
        self.prefs = []
        self.duration_days = None
        self.channel_ids = []


    def generate_queries(self):

        body = {}

        if len(self.channel_ids) > 0:
            body['channel_ids'] = ','.join(self.channel_ids)
        if self.duration_days != None:
            body['duration_days'] = self.duration_days
        if self.prefs != None:
            body['prefs'] = self.prefs
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        if self.query != None:
            body['query'] = self.query
        if self.search_channel_types != None:
            body['search_channel_types'] = self.search_channel_types
        if self.sort != None:
            body['sort'] = self.sort
        if self.sort_dir != None:
            body['sort_dir'] = self.sort_dir
        if self.team_ids != None:
            body['team_ids'] = self.team_ids
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
        self.cursor = None
        self.limit = None
        self.query = None
        self.search_channel_types = None
        self.sort = None
        self.sort_dir = None
        self.team_ids = None