
class SlackClient:

    def __init__(self,clientId):
        self.user = None
        self.clientId = clientId
        self.clientSecret = None
        self.workspaceURL = None
        self.email = None
        self.password = None
        self.token = None
