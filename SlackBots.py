from SlackClient import SlackClient

class SlackBots(SlackClient):

    def __init__(self):
        self.bot = None
        self.team_id = None

    def generate_queries(self):

        body = {}

        if self.bot != None:
            body['bot'] = self.bot
        if self.team_id != None:
            body['team_id'] = self.team_id

        return body

    def clear_queries(self):
        self.bot = None
        self.team_id = None