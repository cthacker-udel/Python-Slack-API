from SlackClient import SlackClient

class SlackAdminAnalytics(SlackClient):

    def __init__(self):
        self.type = None
        self.date = None
        self.metadata_only = None
        self.enterprise_id = None
        self.email_address = None
        self.enterprise_employee_number = None
        self.is_guest = None
        self.is_billable_seat = None
        self.is_active = None
        self.is_active_ios = None
        self.is_active_android = None
        self.is_active_desktop = None
        self.reactions_added_count = None
        self.messages_posted_count = None
        self.channel_messages_posted_count = None
        self.files_added_count = None
        self.is_active_apps = None
        self.is_active_workflows = None
        self.is_active_slack_connect = None
        self.slack_calls_count = None
        self.search_count = None
        self.date_claimed = None


    def generate_queries(self):
        body = {}
        if self.type != None:
            body['type'] = self.type
        if self.date != None:
            body['date'] = self.date
        if self.metadata_only != None:
            body['metadata_only'] = self.metadata_only
        return body