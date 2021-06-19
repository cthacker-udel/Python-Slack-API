from SlackClient import SlackClient

class SlackAdminBarriers(SlackClient):

    def __init__(self):

        self.barriered_from_usergroup_ids = []
        self.primary_usergroup_id = None
        self.restricted_subjects = None
        self.barrier_id = None


    def generate_queries(self):

        body = {}

        if len(self.barriered_from_usergroup_ids) > 0:
            body['barriered_from_usergroup_ids'] = self.barriered_from_usergroup_ids
        if self.primary_usergroup_id != None:
            body['primary_usergroup_id'] = self.primary_usergroup_id
        if self.restricted_subjects != None:
            body['restricted_subjects'] = self.restricted_subjects
        if self.barrier_id != None:
            body['barrier_id'] = self.barrier_id

        return body


    def clear_queries(self):
        self.barriered_from_usergroup_ids = []
        self.primary_usergroup_id = None
        self.restricted_subjects = None
        self.barrier_id = None