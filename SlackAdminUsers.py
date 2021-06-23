from SlackClient import SlackClient

class SlackAdminUsers(SlackClient):

    def __init__(self):
        self.team_id = None
        self.user_id = None
        self.channel_ids = []
        self.is_restricted = None
        self.is_ultra_restricted = None

    def generate_queries(self):
        body = {}
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.user_id != None:
            body['user_id'] = self.user_id
        if len(self.channel_ids) > 0:
            body['channel_ids'] = ','.join(self.channel_ids)
        if self.is_restricted != None:
            body['is_restricted'] = self.is_restricted
        if self.is_ultra_restricted != None:
            body['is_ultra_restricted'] = self.is_ultra_restricted
        return body

    def clear_queries(self):
        self.team_id = None
        self.user_id = None
        self.channel_ids = []
        self.is_restricted = None
        self.is_ultra_restricted = None