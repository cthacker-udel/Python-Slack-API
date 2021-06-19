from SlackClient import SlackClient

class SlackAdmin(SlackClient):

    def __init__(self):
        self.entity_ids = []
        self.entity_type = None
        self.policy_name = None


    def generate_queries(self):

        body = {}

        if len(self.entity_ids) > 0:
            body['entity_ids'] = self.entity_ids
        if self.entity_type != None:
            body['entity_type'] = self.entity_type
        if self.policy_name != None:
            body['policy_name'] = self.policy_name

        return body

    def clear_queries(self):

        self.entity_ids = []
        self.entity_type = None
        self.policy_name = None