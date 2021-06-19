from SlackClient import SlackClient

class SlackAdmin(SlackClient):

    def __init__(self):
        self.entity_ids = []
        self.entity_type = None
        self.policy_name = None
        self.cursor = None
        self.limit = None


    def generate_queries(self):

        body = {}

        if len(self.entity_ids) > 0:
            body['entity_ids'] = self.entity_ids
        if self.entity_type != None:
            body['entity_type'] = self.entity_type
        if self.policy_name != None:
            body['policy_name'] = self.policy_name
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit

        return body

    def clear_queries(self):

        self.entity_ids = []
        self.entity_type = None
        self.policy_name = None
        self.cursor = None
        self.limit = None