
class SlackClient:

    def __init__(self,clientId):
        self.user = None
        self.clientId = clientId
        self.workspaceURL = None
        self.email = None
        self.password = None
