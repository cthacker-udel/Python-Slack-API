from SlackClient import SlackClient

class SlackAdminInviteRequests(SlackClient):

    def __init__(self):
        self.invite_request_id = None
        self.team_id = None
        self.cursor = None
        self.limit = None


    def generate_queries(self):

        body = {}

        if self.invite_request_id != None:
            body['invite_request_id'] = self.invite_request_id
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        return body

    def clear_queries(self):

        self.invite_request_id = None
        self.team_id = None
        self.cursor = None
        self.limit = None