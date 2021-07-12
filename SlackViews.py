from SlackClient import SlackClient

class SlackViews(SlackClient):

    def __init__(self):

        self.trigger_id = None
        self.view = {}
        self.user_id = None
        self.hash = None


    def generate_queries(self):

        body = {}

        if self.trigger_id != None:
            body['trigger_id'] = self.trigger_id
        if 'type' in self.view.keys() and 'title' in self.view.keys() and 'blocks' in self.view.keys():
            body['view'] = self.view
        if self.user_id != None:
            body['user_id'] = self.user_id
        if self.hash != None:
            body['hash'] = self.hash


        return body


    def clear_queries(self):

        self.trigger_id = None
        self.view = {}
        self.user_id = None
        self.hash = None