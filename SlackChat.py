from SlackClient import SlackClient

class SlackChat(SlackClient):

    def __init__(self):
        self.channel = None
        self.ts = None
        self.as_user = None
        self.scheduled_message_id = None
        self.message_ts = None
        self.text = None
        self.attachments = []
        self.user = None
        self.blocks = []
        self.container_id = None
        self.draft_id = None
        self.file_annotation = None
        self.icon_emoji = None
        self.icon_url = None
        self.link_names = None
        self.mrkdwn = None
        self.parse = None
        self.reply_broadcast = None
        self.thread_ts = None
        self.unfurl_links = None
        self.unfurl_media = None
        self.username = None

    def generate_queries(self):

        body = {}

        if len(self.blocks) > 0:
            body['blocks'] = self.blocks
        if self.container_id != None:
            body['container_id'] = self.container_id
        if self.draft_id != None:
            body['draft_id'] = self.draft_id
        if self.file_annotation != None:
            body['file_annotation'] = self.file_annotation
        if self.icon_emoji != None:
            body['icon_emoji'] = self.icon_emoji
        if self.icon_url != None:
            body['icon_url'] = self.icon_url
        if self.link_names != None:
            body['link_names'] = self.link_names
        if self.mrkdwn != None:
            body['mrkdwn'] = self.mrkdwn
        if self.parse != None:
            body['parse'] = self.parse
        if self.reply_broadcast != None:
            body['reply_broadcast'] = self.reply_broadcast
        if self.thread_ts != None:
            body['thread_ts'] = self.thread_ts
        if self.unfurl_links != None:
            body['unfurl_links'] = self.unfurl_links
        if self.unfurl_media != None:
            body['unfurl_media'] = self.unfurl_media
        if self.username != None:
            body['username'] = self.username
        if len(self.attachments) > 0:
            body['attachments'] = self.attachments
        if self.user != None:
            body['user'] = self.user
        if self.message_ts != None:
            body['message_ts'] = self.message_ts
        if self.scheduled_message_id != None:
            body['scheduled_message_id'] = self.scheduled_message_id
        if self.channel != None:
            body['channel'] = self.channel
        if self.ts != None:
            body['ts'] = self.ts
        if self.as_user != None:
            body['as_user'] = self.as_user
        if self.text != None:
            body['text'] = self.text
        return body


    def clear_queries(self):
        self.channel = None
        self.ts = None
        self.as_user = None
        self.scheduled_message_id = None
        self.message_ts = None
        self.text = None
        self.attachments = []
        self.user = None
        self.blocks = []
        self.container_id = None
        self.draft_id = None
        self.file_annotation = None
        self.icon_emoji = None
        self.icon_url = None
        self.link_names = None
        self.mrkdwn = None
        self.parse = None
        self.reply_broadcast = None
        self.thread_ts = None
        self.unfurl_links = None
        self.unfurl_media = None
        self.username = None
