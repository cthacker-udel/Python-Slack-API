from SlackClient import SlackClient

class SlackFiles(SlackClient):

    def __init__(self):
        self.file = None
        self.id = None

        self.count = None
        self.cursor = None
        self.limit = None
        self.page = None

        self.channel = None
        self.show_files_hidden_by_limit = None
        self.ts_from = None
        self.ts_to = None
        self.types = None
        self.user = None

        self.content = None
        self.filename = None
        self.filetype = None
        self.initial_comment = None
        self.thread_ts = None
        self.title = None
        self.channels = []

        self.external_id = None
        self.external_url = None
        self.filetype = None
        self.indexable_file_contents = None
        self.preview_image = None

    def generate_queries(self):

        body = {}

        if self.external_id != None:
            body['external_id'] = self.external_id
        if self.external_url != None:
            body['external_url'] = self.external_url
        if self.title != None:
            body['title'] = self.title
        if self.indexable_file_contents != None:
            body['indexable_file_contents'] = self.indexable_file_contents
        if self.preview_image != None:
            body['preview_image'] = self.preview_image
        if self.filename != None:
            body['filename'] = self.filename
        if self.filetype != None:
            body['filetype'] = self.filetype
        if self.initial_comment != None:
            body['initial_comment'] = self.initial_comment
        if self.tread_ts != None:
            body['thread_ts'] = self.thread_ts
        if self.title != None:
            body['title'] = self.title
        if len(self.channels) > 0:
            body['channels'] = ','.join(self.channels)
        if self.content != None:
            body['content'] = self.content
        if self.channel != None:
            body['channel'] = self.channel
        if self.show_files_hidden_by_limit != None:
            body['show_files_hidden_by_limit'] = self.show_files_hidden_by_limit
        if self.ts_from != None:
            body['ts_from'] = self.ts_from
        if self.ts_to != None:
            body['ts_to'] = self.ts_to
        if self.types != None:
            body['types'] = self.types
        if self.user != None:
            body['user'] = self.user
        if self.file != None:
            body['file'] = self.file
        if self.id != None:
            body['id'] = self.id
        if self.count != None:
            body['count'] = self.count
        if self.cursor != None:
            body['cursor'] = self.cursor
        if self.limit != None:
            body['limit'] = self.limit
        if self.page != None:
            body['page'] = self.page
        return body

    def clear_queries(self):
        self.file = None
        self.id = None
        self.count = None
        self.cursor = None
        self.limit = None
        self.page = None
        self.channel = None
        self.show_files_hidden_by_limit = None
        self.ts_from = None
        self.ts_to = None
        self.types = None
        self.user = None
        self.channels = []
        self.content = None
        self.file = None
        self.filename = None
        self.filetype = None
        self.initial_comment = None
        self.thread_ts = None
        self.title = None
        self.external_id = None
        self.external_url = None
        self.indexable_file_contents = None
        self.preview_image = None

