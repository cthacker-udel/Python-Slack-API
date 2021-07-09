from SlackClient import SlackClient

class SlackTeam(SlackClient):

    def __init__(self):
        self.before = None
        self.count = None
        self.page = None
        self.team_id = None
        self.user = None
        self.team = None
        self.app_id = None
        self.change_type = None
        self.service_id = None
        self.team_id = None
        self.visibility = None


    def generate_queries(self):

        queries = {}

        if self.visibility != None:
            queries['visibility'] = self.visibility
        if self.app_id != None:
            queries['app_id'] = self.app_id
        if self.change_type != None:
            queries['change_type'] = self.change_type
        if self.service_id != None:
            queries['service_id'] = self.service_id
        if self.team_id != None:
            queries['team_id'] = self.team_id
        if self.before != None:
            queries['before'] = self.before
        if self.count != None:
            queries['count'] = self.count
        if self.page != None:
            queries['page'] = self.page
        if self.team_id != None:
            queries['team_id'] = self.team_id
        if self.user != None:
            queries['user'] = self.user
        if self.team != None:
            queries['team'] = self.team


        return queries

    def clear_queries(self):
        self.team = None
        self.before = None
        self.count = None
        self.page = None
        self.team_id = None
        self.user = None
        self.app_id = None
        self.change_type = None
        self.service_id = None
        self.team_id = None
        self.visibility = None