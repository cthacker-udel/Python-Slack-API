from SlackClient import SlackClient

class SlackMigration(SlackClient):

    def __init__(self):
        self.users = []
        self.team_id = None
        self.to_old = None

    def generate_queries(self):

        body = {}

        if self.users != None:
            body['users'] = ','.join(self.users)
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.to_old != None:
            body['to_old'] = self.to_old
        return body

    def clear_queries(self):

        self.users = []
        self.team_id = None
        self.to_old = None