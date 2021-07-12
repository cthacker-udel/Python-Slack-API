from SlackClient import SlackClient

class SlackViews(SlackClient):

    def __init__(self):

        self.trigger_id = None
        self.view = {}


    def generate_queries(self):

        body = {}

        if self.trigger_id != None:
            body['trigger_id'] = self.trigger_id
        if 'type' in self.view.keys() and 'title' in self.view.keys() and 'blocks' in self.view.keys():
            body['view'] = self.view

        return body


    def clear_queries(self):

        self.trigger_id = None
        self.view = {}