from SlackClient import SlackClient

class SlackReminders(SlackClient):

    def __init__(self):

        self.text = None
        self.time = None
        self.team_id = None
        self.user = None


    def generate_queries(self):

        body = {}

        if self.text != None:
            body['text'] = self.text
        if self.time != None:
            body['time'] = self.time
        if self.team_id != None:
            body['team_id'] = self.team_id
        if self.user != None:
            body['user'] = self.user
        return body

    def clear_queries(self):

        self.text = None
        self.time = None
        self.team_id = None
        self.user = None
