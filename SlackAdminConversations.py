from SlackClient import SlackClient

class SlackAdminConversations(SlackClient):

    def __init__(self):
        self.channel_id = None


    def generate_queries(self):

        body = {}

        if self.channel_id != None:
            body['channel_id'] = self.channel_id

        return body

    def clear_queries(self):
        self.channel_id = None