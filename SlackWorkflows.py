from SlackClient import SlackClient


class SlackWorkflows(SlackClient):

    def __init__(self):

        self.workflow_step_execute_id = None
        self.outputs = None
        self.inputs = None
        self.step_image_url = None
        self.step_name = None

    def generate_queries(self):

        body = {}

        if self.workflow_step_execute_id != None:
            body['workflow_step_execute_id'] = self.workflow_step_execute_id
        if self.outputs != None:
            body['outputs'] = self.outputs
        if self.inputs != None:
            body['inputs'] = self.inputs
        if self.step_image_url != None:
            body['step_image_url'] = self.step_image_url
        if self.step_name != None:
            body['step_name'] = self.step_name
        return body

    def clear_queries(self):

        self.workflow_step_execute_id = None
        self.outputs = None
        self.inputs = None
        self.step_image_url = None
        self.step_name = None