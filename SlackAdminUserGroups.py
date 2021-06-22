from SlackClient import SlackClient

class SlackAdminUserGroups(SlackClient):

    def __init__(self):
        self.channel_ids = []
        self.usergroup_id = None
        self.team_id = None
        self.team_ids = []
        self.auto_provision = None
        self.include_num_members = None


    def generate_queries(self):

        body = {}

        if self.include_members != None:
            body['include_num_members'] = self.include_num_members
        if len(self.channel_ids) > 0:
            body['channel_ids'] = ','.join(self.channel_ids)
        if self.usergroup_id != None:
            body['usergroup_id'] = self.usergroup_id
        if self.team_id != None:
            body['team_id'] = self.team_id
        if len(self.team_ids) > 0:
            body['team_ids'] = ','.join(self.team_ids)
        if self.auto_provision != None:
            body['auto_provision'] = self.auto_provision

        return body

    def clear_queries(self):

        self.channel_ids = []
        self.usergroup_id = None
        self.team_id = None
        self.team_ids = []
        self.auto_provision = None
        self.include_num_members = None