from SlackClient import SlackClient

class SlackDialog(SlackClient):

    def __init__(self):

        self.dialog = None
        self.trigger_id = None

    def generate_queries(self):

        body = {}

        if self.dialog != None:
            body['dialog'] = self.dialog
        if self.trigger_id != None:
            body['trigger_id'] = self.trigger_id

        return body

    def clear_queries(self):
        self.dialog = None
        self.trigger_id = None