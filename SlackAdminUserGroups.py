from SlackClient import SlackClient

class SlackAdminUserGroups(SlackClient):

    def __init__(self):
        self.channel_ids = []
        self.usergroup_id = None
        self.team_id = None


    def generate_queries(self):

        body = {}

        if len(self.channel_ids) > 0:
            body['channel_ids'] = ','.join(self.channel_ids)
        if self.usergroup_id != None:
            body['usergroup_id'] = self.usergroup_id
        if self.team_id != None:
            body['team_id'] = self.team_id

        return body

    def clear_queries(self):
        self.channel_ids = []
        self.usergroup_id = None
        self.team_id = None