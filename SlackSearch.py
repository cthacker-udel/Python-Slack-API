from SlackClient import SlackClient

class SlackSearch(SlackClient):

    def __init__(self):

        self.query = None
        self.count = None
        self.highlight = None
        self.page = None
        self.sort = None
        self.sort_dir = None
        self.team_id = None


    def generate_queries(self):

        body = {}

        if self.query != None:
            body['query'] = self.query
        if self.count != None:
            body['count'] = self.count
        if self.highlight != None:
            body['highlight'] = self.highlight
        if self.page != None:
            body['page'] = self.page
        if self.sort != None:
            body['sort'] = self.sort
        if self.sort_dir != None:
            body['sort_dir'] = self.sort_dir
        if self.team_id != None:
            body['team_id'] = self.team_id
        return body

    def clear_queries(self):

        self.query = None
        self.count = None
        self.highlight = None
        self.page = None
        self.sort = None
        self.sort_dir = None
        self.team_id = None