from SlackClient import SlackClient

class SlackAdminApps(SlackClient):

    def __init__(self):
        self.app_id = None
        self.enterprise_id = None
        self.request_id = None
        self.team_id = None

    def generate_queries(self):

        body = {}

        if self.app_id != None:
            body['app_id'] = self.app_id
        if self.enterprise_id != None:
            body['enterprise_id'] = self.enterprise_id
        if self.request_id != None:
            body['request_id'] = self.request_id
        if self.team_id != None:
            body['team_id'] = self.team_id
        return body

    def clear_queries(self):
        self.app_id = None
        self.enterprise_id = None
        self.request_id = None
        self.team_id = None