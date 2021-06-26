from SlackClient import SlackClient
import requests
from pprint import pprint
import urllib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from selenium_stealth import stealth
import time


base_url = 'https://slack.com/api'

class OauthMethods(SlackClient):

    def __init__(self,slackclient):
        self.client = slackclient
        self.scopes = []



    def generate_redirect(self):

        try:
            br = webdriver.Firefox(FirefoxDriverManager().install())
        except Exception as e:
            try:
                br = webdriver.Chrome(ChromeDriverManager().install())
            except Exception as e:
                return None

        scopes_string = ','.join(self.scopes)
        url = 'https://slack.com/oauth/v2/authorize?scope={}&client_id={}'.format(scopes_string,self.client.clientId)
        br.get(url)
        time.sleep(100)
        br.find_element_by_id('domain').send_keys(self.client.workspaceURL)
        br.find_element_by_xpath('//*[@id="page_contents"]/div/div/div[1]/div[2]/form/button').click()
        br.find_element_by_id('email').send_keys(self.client.email)
        br.find_element_by_id('password').send_keys(self.client.password)
        br.find_element_by_id('signin_btn').click()


class AdminAnalytics(SlackClient):

    def __init__(self,client):
        self.client = client


    def getFile(self):

        url = base_url + '/admin.analytics.getFile'

        body = self.client.SlackAdminAnalytics.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

class AdminApps(SlackClient):

    def __init__(self,client):
        self.client = client

    def approve_app_installation(self):

        url = base_url + '/admin.apps.approve'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def clear_app_resolution(self):

        url = base_url + '/admin.apps.clearResolution'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def restrict_app_installation(self):

        url = base_url + '/admin.apps.restrict'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def uninstall_app(self):

        url = base_url + '/admin.apps.uninstall'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_approved_apps(self):

        url = base_url + '/admin.apps.approved.list'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def list_pending_app_installation(self):

        url = base_url + '/admin.apps.requests.list'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def list_restricted_apps(self):

        url = base_url + '/admin.apps.restricted.list'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)


class AdminAuth(SlackClient):

    def __init__(self,client):
        self.client = client


    def assign_entities(self):

        url = base_url + '/admin.auth.policy.assignEntities'

        body = self.client.SlackAdminAuth.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def fetch_all_entities(self):

        url = base_url + '/admin.auth.policy.getEntities'

        body = self.client.SlackAdminAuth.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)


    def remove_specified_entities(self):

        url = base_url + '/admin.auth.policy.removeEntities'

        body = self.client.SlackAdminAuth.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

class AdminBarriers(SlackClient):

    def __init__(self,client):
        self.client = client


    def create_information_barrier(self):

        url = base_url + '/admin.barriers.create'

        body = self.client.SlackAdminBarriers.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def delete_existing_information_barrier(self):

        url = base_url + '/admin.barriers.delete'

        body = self.client.SlackAdminBarriers.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def get_all_information_barriers(self):

        url = base_url + '/admin.barriers.list'

        body = self.client.SlackAdminBarriers.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def update_existing_information_barrier(self):

        url = base_url + '/admin.barriers.update'

        body = self.client.SlackAdminBarriers.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)


class AdminConversations(SlackClient):

    def __init__(self,client):
        self.client = client

    def archive_conversation(self):

        url = base_url + '/admin.conversations.archive'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)


    def convert_public_channel_to_private(self):

        url = base_url + '/admin.conversations.convertToPrivate'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def create_public_or_private_channel(self):

        url = base_url + '/admin.conversations.create'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def delete_public_or_private(self):

        url = base_url + '/admin.conversations.delete'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)


    def get_conversation_preferences_for_public_or_private_channel(self):

        url = base_url + '/admin.conversations.getConversationPrefs'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def get_channels_retention_policy(self):

        url = base_url + '/admin.conversations.getCustomRetention'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def get_all_workspaces_within_enterprise_org(self):

        url = base_url + '/admin.conversations.getTeams'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def invite_user_to_channel(self):

        url = base_url + '/admin.conversations.invite'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def remove_custom_retention(self):

        url = base_url + '/admin.conversations.removeCustomRetention'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def rename_channel(self):

        url = base_url + '/admin.conversations.rename'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def search_enterprise_channel(self):

        url = base_url + '/admin.conversations.search'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_channel_posting_permissions(self):

        url = base_url + '/admin.conversations.setConversationPrefs'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_channel_retention_policy(self):

        url = base_url + '/admin.conversations.setCustomRetention'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_workspaces_in_enterprise_org(self):

        url = base_url + '/admin.conversations.setTeams'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def unarchive_channel(self):

        url = base_url + '/admin.conversations.unarchive'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_all_disconnected_channels(self):

        url = base_url + '/admin.conversations.ekm.listOriginalConnectedChannelInfo'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def add_channel_allowlist(self):

        url = base_url + '/admin.conversations.restrictAccess.addGroup'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def list_channel_groups(self):

        url = base_url + '/admin.conversations.restrictAccess.listGroups'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def remove_private_channel_group(self):

        url = base_url + '/admin.conversations.restrictAccess.removeGroup'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

class AdminEmoji(SlackClient):

    def __init__(self,client):
        self.client = client


    def add_emoji(self):

        url = base_url + '/admin.emoji.add'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def add_emoji_alias(self):

        url = base_url + '/admin.emoji.addAlias'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def list_emojis(self):

        url = base_url + '/admin.emoji.list'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def remove_emoji(self):

        url = base_url + '/admin.emoji.remove'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def rename_emoji(self):

        url = base_url + '/admin.emoji.rename'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)


class AdminInviteRequests(SlackClient):

    def __init__(self,client):
        self.client = client


    def approve_request(self):

        url = base_url + '/admin.inviteRequests.approve'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def deny_request(self):

        url = base_url + '/admin.inviteRequests.deny'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_requests(self):

        url = base_url + '/admin.inviteRequests.list'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_approved_requests(self):

        url = base_url + '/admin.inviteRequests.approved.list'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_denied_requests(self):

        url = base_url + '/admin.inviteRequests.denied.list'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

class AdminTeams(SlackClient):

    def __init__(self,client):
        self.client = client


    def list_admins(self):

        url = base_url + '/admin.teams.admins.list'

        body = self.client.SlackTeams.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def create_enterprise_team(self):

        url = base_url + '/admin.teams.create'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_enterprise_teams(self):

        url = base_url + '/admin.teams.list'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_workspace_owners(self):

        url = base_url + '/admin.teams.owners.list'

        body = self.client.SlackTeams.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def fetch_workspace_settings(self):

        url = base_url + '/admin.teams.settings.info'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_default_workspace_channels(self):

        url = base_url + '/admin.teams.settings.setDefaultChannels'

        body = self.client.SlackTeams.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def set_workspace_description(self):

        url = base_url + '/admin.team.settings.setDescription'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_workspace_discoverability(self):

        url = base_url + '/admin.teams.settings.setDiscoverability'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_workspace_icons(self):

        url = base_url + '/admin.teams.settings.setIcon'

        body = self.client.SlackTeams.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def set_workspace_name(self):

        url = base_url + '/admin.teams.settings.setName'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)


class AdminUserGroups(SlackClient):

    def __init__(self,client):
        self.client = client

    def add_idp_group_channel(self):

        url = base_url + '/admin.usergroups.addChannels'

        body = self.client.SlackAdminUserGroups.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def associate_workspace_to_idp(self):

        url = base_url + '/admin.usergroups.addTeams'

        body = self.client.SlackAdminUserGroups.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_idp_channels(self):

        url = base_url + '/admin.usergroups.listChannels'

        body = self.client.SlackAdminUserGroups.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)


    def remove_idp_channel(self):

        url = base_url + '/admin.usergroups.removeChannels'

        body = self.client.SlackAdminUserGroups.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)


class AdminUsers(SlackClient):

    def __init__(self,client):
        self.client = client

    def add_user_to_workspace(self):

        url = base_url + '/admin.users.assign'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def invite_user_to_workspace(self):

        url = base_url + '/admin.users.invite'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_workspace_users(self):

        url = base_url + '/admin.users.list'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def remove_workspace_user(self):

        url = base_url + '/admin.users.remove'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_admin(self):

        url = base_url + '/admin.users.setAdmin'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_user_expiration(self):

        url = base_url + '/admin.users.setExpiration'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_owner(self):

        url = base_url + '/admin.users.setOwner'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def set_regular_user(self):

        url = base_url + '/admin.users.setRegular'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def clear_user_session_settings(self):

        url = base_url + '/admin.users.session.clearSettings'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def get_user_session_settings(self):

        url = base_url + '/admin.users.session.getSettings'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)


    def revoke_user_session(self):

        url = base_url + '/admin.users.session.invalidate'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def list_active_users(self):

        url = base_url + '/admin.users.session.list'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def reset_all_sessions(self):

        url = base_url + '/admin.users.session.reset'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def configure_user_settings(self):

        url = base_url + '/admin.users.session.setSettings'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)


class SlackApi(SlackClient):

    def __init__(self,client):
        self.client = client

    def check_api_calling_code(self):

        url = base_url + '/api/api.test'

        body = self.client.SlackAPI.generate_queries()

        request = requests.post(url, auth=self.client.token, json=body)

        pprint(request)


class SlackApps(SlackClient):

    def __init__(self,client):
        self.client = client

    def generate_websocket_url(self):

        url = base_url + '/apps.connections.open'

        request = requests.post(url,auth=self.client.token)

        pprint(request)

    def get_authorization_list(self):

        url = base_url + '/apps.event.authorization.list'

        body = self.client.SlackApps.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def uninstall_app(self):

        url = base_url + '/apps.uninstall'

        body = self.client.SlackApps.generate_queries()

        request = requests.post(url, auth=self.client.token, json=body)

        pprint(request)

class SlackAuth(SlackClient):

    def __init__(self,client):
        self.client = client


    def revoke_token(self):

        url = base_url + '/auth.revoke'

        body = self.client.SlackAuth.generate_queries()

        request = requests.get(url, auth=self.client.token, params=body)

        pprint(request)

    def check_token(self):

        url = base_url + '/auth.test'

        body = self.client.SlackAuth.generate_queries()

        request = requests.post(url, auth=self.client.token, json=body)

        pprint(request)

    def list_token_workspace_access(self):

        url = base_url + '/auth.teams.list'

        body = self.client.SlackAuth.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)


class SlackBots(SlackClient):

    def __init__(self,client):
        self.client = client


    def get_bot_info(self):

        url = base_url + '/bots.info'

        body = self.client.SlackBots.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

class SlackCalls(SlackClient):

    def __init__(self,client):
        self.client = client

    def register_new_call(self):

        url = base_url + '/calls.add'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def end_call(self):

        url = base_url + '/calls.end'

        body = self.client.SlackCall.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def get_call_info(self):

        url = base_url + '/calls.info'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def update_call_information(self):

        url = base_url + '/calls.update'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def add_call_participant(self):

        url = base_url + '/calls.participants.add'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def remove_call_participant(self):

        url = base_url + '/calls.participants.remove'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

class SlackChat(SlackClient):

    def __init__(self,client):
        self.client = client

    def delete_message(self):

        url = base_url + '/chat.delete'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def delete_scheduled_message(self):

        url = base_url + '/chat.deleteScheduledMessage'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def get_chat_permalink(self):

        url = base_url + '/chat.getPermalink'

        body = self.client.SlackChat.generate_queries()

        request = requests.get(url,auth=self.client.token,params=body)

        pprint(request)

    def share_chat_me_message(self):

        url = base_url + '/chat.meMessage'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def send_ephemeral_message(self):

        url = base_url + '/chat.postEphemeral'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)

    def send_message(self):

        url = base_url + '/chat.postMessage'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=self.client.token,json=body)

        pprint(request)























def main():

    client = SlackClient('636558213122.2172017410279')
    oauthRequests = OauthMethods(client)
    oauthRequests.scopes.append('incoming-webhook')
    oauthRequests.scopes.append('commands')
    oauthRequests.generate_redirect()


if __name__ == '__main__':
    main()