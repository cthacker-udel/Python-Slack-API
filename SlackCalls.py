from SlackClient import SlackClient

class SlackCalls(SlackClient):

    def __init__(self):
        self.external_unique_id = None
        self.join_url = None
        self.created_by = None
        self.date_start = None
        self.desktop_app_join_url = None
        self.external_display_id = None
        self.title = None
        self.users = None

    def generate_queries(self):

        body = {}

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