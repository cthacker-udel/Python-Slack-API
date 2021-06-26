from SlackClient import SlackClient

class SlackChat(SlackClient):

    def __init__(self):
        self.channel = None
        self.ts = None
        self.as_user = None
        self.scheduled_message_id = None
        self.message_ts = None
        self.text = None

    def generate_queries(self):

        body = {}

        if self.message_ts != None:
            body['message_ts'] = self.message_ts
        if self.scheduled_message_id != None:
            body['scheduled_message_id'] = self.scheduled_message_id
        if self.channel != None:
            body['channel'] = self.channel
        if self.ts != None:
            body['ts'] = self.ts
        if self.as_user != None:
            body['as_user'] = self.as_user
        if self.text != None:
            body['text'] = self.text
        return body


    def clear_queries(self):
        self.channel = None
        self.ts = None
        self.as_user = None
        self.scheduled_message_id = None
        self.message_ts = None
        self.text = None
