from SlackClient import SlackClient

class SlackCalls(SlackClient):

    class SlackCallUser(SlackClient):

        def __init__(self):
            self.slack_id = None
            self.external_id = None
            self.display_name = None
            self.avatar_url = None

        def generate_json_user(self):

            body = {}
            if self.slack_id != None:
                body['slack_id'] = self.slack_id
            if self.external_id != None:
                body['external_id'] = self.external_id
            if self.avatar_url != None:
                body['avatar_url'] = self.avatar_url
            return body

    def __init__(self):
        self.external_unique_id = None
        self.join_url = None
        self.created_by = None
        self.date_start = None
        self.desktop_app_join_url = None
        self.external_display_id = None
        self.title = None
        self.users = None
        self.id = None
        self.duration = None
        self.users = []

    def generate_queries(self):

        body = {}

        if len(self.users) > 0:
            body['users'] = self.users
        if self.id != None:
            body['id'] = self.id
        if self.duration != None:
            body['duration'] = self.duration
        if self.external_unique_id != None:
            body['external_unique_id'] = self.external_unique_id
        if self.join_url != None:
            body['join_url'] = self.join_url
        if self.created_by != None:
            body['created_by'] = self.created_by
        if self.date_start != None:
            body['date_start'] = self.date_start
        if self.desktop_app_join_url != None:
            body['desktop_app_join_url'] = self.desktop_app_join_url
        if self.external_display_id != None:
            body['external_display_id'] = self.external_display_id
        if self.title != None:
            body['title'] = self.title
        if self.users != None:
            body['users'] = self.users

    def clear_queries(self):
        self.external_unique_id = None
        self.join_url = None
        self.created_by = None
        self.date_start = None
        self.desktop_app_join_url = None
        self.external_display_id = None
        self.title = None
        self.users = None
        self.id = None
        self.duration = None