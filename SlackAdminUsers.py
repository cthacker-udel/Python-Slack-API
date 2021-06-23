from SlackClient import SlackClient

class SlackAdminUsers(SlackClient):

    def __init__(self):
        self.team_id = None
        self.user_id = None
        self.channel_ids = []
        self.is_restricted = None
        self.is_ultra_restricted = None
        self.email = None
        self.custom_message = None
        self.guest_expiration_ts = None
        self.real_name = None
        self.resend = None
        self.cursor = None
        self.limit = None
        self.expiration_ts = None
        self.user_ids = []

    def generate_queries(self):
        body = {}

        if len(self.user_ids) > 0:
            body['user_ids'] = self.user_ids
        if self.expiration_ts != None:
            body['expiration_ts'] = self.expiration_ts
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
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
        if self.email != None:
            body['email'] = self.email
        if self.custom_message != None:
            body['custom_message'] = self.custom_message
        if self.guest_expiration_ts != None:
            body['guest_expiration_ts'] = self.guest_expiration_ts
        if self.real_name != None:
            body['real_name'] = self.real_name
        if self.resend != None:
            body['resend'] = self.resend;
        return body

    def clear_queries(self):
        self.team_id = None
        self.user_id = None
        self.channel_ids = []
        self.is_restricted = None
        self.is_ultra_restricted = None
        self.email = None
        self.custom_message = None
        self.guest_expiration_ts = None
        self.real_name = None
        self.resend = None
        self.cursor = None
        self.limit = None
        self.expiration_ts = None