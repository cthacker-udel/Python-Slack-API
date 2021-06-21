from SlackClient import SlackClient

class SlackAdminInviteRequests(SlackClient):

    def __init__(self):
        self.invite_request_id = None
        self.team_id = None


    def generate_queries(self):

        body = {}

        if self.invite_request_id != None:
            body['invite_request_id'] = self.invite_request_id
        if self.team_id != None:
            body['team_id'] = self.team_id
        return body

    def clear_queries(self):

        self.invite_request_id = None
        self.team_id = None