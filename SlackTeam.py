from SlackClient import SlackClient

class SlackTeam(SlackClient):

    def __init__(self):
        self.before = None
        self.count = None
        self.page = None
        self.team_id = None
        self.user = None


    def generate_queries(self):

        queries = {}

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

        return queries

    def clear_queries(self):
        self.before = None
        self.count = None
        self.page = None
        self.team_id = None
        self.user = None