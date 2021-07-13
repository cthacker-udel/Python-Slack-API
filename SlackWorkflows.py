from SlackClient import SlackClient


class SlackWorkflows(SlackClient):

    def __init__(self):

        self.workflow_step_execute_id = None
        self.outputs = None

    def generate_queries(self):

        body = {}

        if self.workflow_step_execute_id != None:
            body['workflow_step_execute_id'] = self.workflow_step_execute_id
        if self.outputs != None:
            body['outputs'] = self.outputs
        return body

    def clear_queries(self):

        self.workflow_step_execute_id = None
        self.outputs = None