from SlackClient import SlackClient
import requests
from pprint import pprint
import urllib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from selenium_stealth import stealth
import time
from requests.auth import HTTPBasicAuth


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

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

class AdminApps(SlackClient):

    def __init__(self,client):
        self.client = client

    def approve_app_installation(self):

        url = base_url + '/admin.apps.approve'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def clear_app_resolution(self):

        url = base_url + '/admin.apps.clearResolution'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def restrict_app_installation(self):

        url = base_url + '/admin.apps.restrict'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def uninstall_app(self):

        url = base_url + '/admin.apps.uninstall'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_approved_apps(self):

        url = base_url + '/admin.apps.approved.list'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_pending_app_installation(self):

        url = base_url + '/admin.apps.requests.list'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_restricted_apps(self):

        url = base_url + '/admin.apps.restricted.list'

        body = self.client.SlackAdminApps.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class AdminAuth(SlackClient):

    def __init__(self,client):
        self.client = client


    def assign_entities(self):

        url = base_url + '/admin.auth.policy.assignEntities'

        body = self.client.SlackAdminAuth.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def fetch_all_entities(self):

        url = base_url + '/admin.auth.policy.getEntities'

        body = self.client.SlackAdminAuth.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


    def remove_specified_entities(self):

        url = base_url + '/admin.auth.policy.removeEntities'

        body = self.client.SlackAdminAuth.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

class AdminBarriers(SlackClient):

    def __init__(self,client):
        self.client = client


    def create_information_barrier(self):

        url = base_url + '/admin.barriers.create'

        body = self.client.SlackAdminBarriers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def delete_existing_information_barrier(self):

        url = base_url + '/admin.barriers.delete'

        body = self.client.SlackAdminBarriers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_all_information_barriers(self):

        url = base_url + '/admin.barriers.list'

        body = self.client.SlackAdminBarriers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def update_existing_information_barrier(self):

        url = base_url + '/admin.barriers.update'

        body = self.client.SlackAdminBarriers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class AdminConversations(SlackClient):

    def __init__(self,client):
        self.client = client

    def archive_conversation(self):

        url = base_url + '/admin.conversations.archive'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


    def convert_public_channel_to_private(self):

        url = base_url + '/admin.conversations.convertToPrivate'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def create_public_or_private_channel(self):

        url = base_url + '/admin.conversations.create'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def delete_public_or_private(self):

        url = base_url + '/admin.conversations.delete'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


    def get_conversation_preferences_for_public_or_private_channel(self):

        url = base_url + '/admin.conversations.getConversationPrefs'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_channels_retention_policy(self):

        url = base_url + '/admin.conversations.getCustomRetention'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_all_workspaces_within_enterprise_org(self):

        url = base_url + '/admin.conversations.getTeams'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def invite_user_to_channel(self):

        url = base_url + '/admin.conversations.invite'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def remove_custom_retention(self):

        url = base_url + '/admin.conversations.removeCustomRetention'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def rename_channel(self):

        url = base_url + '/admin.conversations.rename'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def search_enterprise_channel(self):

        url = base_url + '/admin.conversations.search'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_channel_posting_permissions(self):

        url = base_url + '/admin.conversations.setConversationPrefs'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_channel_retention_policy(self):

        url = base_url + '/admin.conversations.setCustomRetention'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_workspaces_in_enterprise_org(self):

        url = base_url + '/admin.conversations.setTeams'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def unarchive_channel(self):

        url = base_url + '/admin.conversations.unarchive'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_all_disconnected_channels(self):

        url = base_url + '/admin.conversations.ekm.listOriginalConnectedChannelInfo'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def add_channel_allowlist(self):

        url = base_url + '/admin.conversations.restrictAccess.addGroup'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_channel_groups(self):

        url = base_url + '/admin.conversations.restrictAccess.listGroups'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def remove_private_channel_group(self):

        url = base_url + '/admin.conversations.restrictAccess.removeGroup'

        body = self.client.SlackAdminConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

class AdminEmoji(SlackClient):

    def __init__(self,client):
        self.client = client


    def add_emoji(self):

        url = base_url + '/admin.emoji.add'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def add_emoji_alias(self):

        url = base_url + '/admin.emoji.addAlias'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_emojis(self):

        url = base_url + '/admin.emoji.list'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def remove_emoji(self):

        url = base_url + '/admin.emoji.remove'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def rename_emoji(self):

        url = base_url + '/admin.emoji.rename'

        body = self.client.SlackAdminEmoji.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class AdminInviteRequests(SlackClient):

    def __init__(self,client):
        self.client = client


    def approve_request(self):

        url = base_url + '/admin.inviteRequests.approve'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def deny_request(self):

        url = base_url + '/admin.inviteRequests.deny'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_requests(self):

        url = base_url + '/admin.inviteRequests.list'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_approved_requests(self):

        url = base_url + '/admin.inviteRequests.approved.list'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_denied_requests(self):

        url = base_url + '/admin.inviteRequests.denied.list'

        body = self.client.SlackAdminInviteRequests.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

class AdminTeams(SlackClient):

    def __init__(self,client):
        self.client = client


    def list_admins(self):

        url = base_url + '/admin.teams.admins.list'

        body = self.client.SlackTeams.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def create_enterprise_team(self):

        url = base_url + '/admin.teams.create'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_enterprise_teams(self):

        url = base_url + '/admin.teams.list'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_workspace_owners(self):

        url = base_url + '/admin.teams.owners.list'

        body = self.client.SlackTeams.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def fetch_workspace_settings(self):

        url = base_url + '/admin.teams.settings.info'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_default_workspace_channels(self):

        url = base_url + '/admin.teams.settings.setDefaultChannels'

        body = self.client.SlackTeams.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def set_workspace_description(self):

        url = base_url + '/admin.team.settings.setDescription'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_workspace_discoverability(self):

        url = base_url + '/admin.teams.settings.setDiscoverability'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_workspace_icons(self):

        url = base_url + '/admin.teams.settings.setIcon'

        body = self.client.SlackTeams.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def set_workspace_name(self):

        url = base_url + '/admin.teams.settings.setName'

        body = self.client.SlackTeams.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class AdminUserGroups(SlackClient):

    def __init__(self,client):
        self.client = client

    def add_idp_group_channel(self):

        url = base_url + '/admin.usergroups.addChannels'

        body = self.client.SlackAdminUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def associate_workspace_to_idp(self):

        url = base_url + '/admin.usergroups.addTeams'

        body = self.client.SlackAdminUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_idp_channels(self):

        url = base_url + '/admin.usergroups.listChannels'

        body = self.client.SlackAdminUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


    def remove_idp_channel(self):

        url = base_url + '/admin.usergroups.removeChannels'

        body = self.client.SlackAdminUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class AdminUsers(SlackClient):

    def __init__(self,client):
        self.client = client

    def add_user_to_workspace(self):

        url = base_url + '/admin.users.assign'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def invite_user_to_workspace(self):

        url = base_url + '/admin.users.invite'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_workspace_users(self):

        url = base_url + '/admin.users.list'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def remove_workspace_user(self):

        url = base_url + '/admin.users.remove'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_admin(self):

        url = base_url + '/admin.users.setAdmin'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_user_expiration(self):

        url = base_url + '/admin.users.setExpiration'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_owner(self):

        url = base_url + '/admin.users.setOwner'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_regular_user(self):

        url = base_url + '/admin.users.setRegular'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def clear_user_session_settings(self):

        url = base_url + '/admin.users.session.clearSettings'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_user_session_settings(self):

        url = base_url + '/admin.users.session.getSettings'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


    def revoke_user_session(self):

        url = base_url + '/admin.users.session.invalidate'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_active_users(self):

        url = base_url + '/admin.users.session.list'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def reset_all_sessions(self):

        url = base_url + '/admin.users.session.reset'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def configure_user_settings(self):

        url = base_url + '/admin.users.session.setSettings'

        body = self.client.SlackAdminUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class SlackApi(SlackClient):

    def __init__(self,client):
        self.client = client

    def check_api_calling_code(self):

        url = base_url + '/api/api.test'

        body = self.client.SlackAPI.generate_queries()

        request = requests.post(url, auth=HTTPBasicAuth('',self.client.token), json=body)

        pprint(request)


class SlackApps(SlackClient):

    def __init__(self,client):
        self.client = client

    def return_team_permissions(self):

        url = base_url + '/apps.permissions.info'

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token))

        pprint(request)

    def generate_websocket_url(self):

        url = base_url + '/apps.connections.open'

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token))

        pprint(request)

    def get_authorization_list(self):

        url = base_url + '/apps.event.authorization.list'

        body = self.client.SlackApps.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def uninstall_app(self):

        url = base_url + '/apps.uninstall'

        body = self.client.SlackApps.generate_queries()

        request = requests.post(url, auth=HTTPBasicAuth('',self.client.token), json=body)

        pprint(request)

    def allows_app_request_scopes(self):

        url = base_url + '/apps.permissions.request'

        body = self.client.SlackApps.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def return_team_resource_grants(self):

        url = base_url + '/apps.permissions.resources.list'

        body = self.client.SlackApps.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def return_team_scopes(self):

        url = base_url + '/apps.permissions.scopes.list'

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token))

        pprint(request)

    def return_user_grants_and_scopes(self):

        url = base_url + '/apps.permissions.users.list'

        body = self.client.SlackApps.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def enable_app_user_access(self):

        url = base_url + '/apps.permissions.users.request'

        body = self.client.SlackApps.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class SlackAuth(SlackClient):

    def __init__(self,client):
        self.client = client


    def revoke_token(self):

        url = base_url + '/auth.revoke'

        body = self.client.SlackAuth.generate_queries()

        request = requests.get(url, auth=HTTPBasicAuth('',self.client.token), params=body)

        pprint(request)

    def check_token(self):

        url = base_url + '/auth.test'

        body = self.client.SlackAuth.generate_queries()

        request = requests.post(url, auth=HTTPBasicAuth('',self.client.token), json=body)

        pprint(request)

    def list_token_workspace_access(self):

        url = base_url + '/auth.teams.list'

        body = self.client.SlackAuth.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class SlackBots(SlackClient):

    def __init__(self,client):
        self.client = client


    def get_bot_info(self):

        url = base_url + '/bots.info'

        body = self.client.SlackBots.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

class SlackCalls(SlackClient):

    def __init__(self,client):
        self.client = client

    def register_new_call(self):

        url = base_url + '/calls.add'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def end_call(self):

        url = base_url + '/calls.end'

        body = self.client.SlackCall.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_call_info(self):

        url = base_url + '/calls.info'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def update_call_information(self):

        url = base_url + '/calls.update'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def add_call_participant(self):

        url = base_url + '/calls.participants.add'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def remove_call_participant(self):

        url = base_url + '/calls.participants.remove'

        body = self.client.SlackCalls.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class SlackChannels(SlackClient):

    def __init__(self,client):
        self.client = client

    def archive_channel(self):

        url = base_url + '/channels.archive'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def create_channel(self):

        url = base_url + '/channels.create'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def fetch_channel_message_event_history(self):

        url = base_url + '/channels.history'

        body = self.client.SlackChannels.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_channel_information(self):

        url = base_url + '/channels.info'

        body = self.client.SlackChannels.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def invite_user_to_channel(self):

        url = base_url + '/channels.invite'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def join_or_create_channel(self):

        url = base_url + '/channels.join'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def remove_channel_user(self):

        url = base_url + '/channels.kick'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def leave_channel(self):

        url = base_url + '/channels.leave'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_team_channels(self):

        url = base_url + '/channels.list'

        body = self.client.SlackChannels.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def set_channel_read_cursor(self):

        url = base_url + '/channels.mark'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def rename_channel(self):

        url = base_url + '/channels.rename'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def retrieve_channel_message_thread(self):

        url = base_url + '/channels.replies'

        body = self.client.SlackChannels.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def set_channel_purpose(self):

        url = base_url + '/channels.setPurpose'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def set_channel_topic(self):

        url = base_url + '/channels.setTopic'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def unarchive_channel(self):

        url = base_url + '/channels.unarchive'

        body = self.client.SlackChannels.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

class SlackChat(SlackClient):

    def __init__(self,client):
        self.client = client

    def delete_message(self):

        url = base_url + '/chat.delete'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def delete_scheduled_message(self):

        url = base_url + '/chat.deleteScheduledMessage'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_chat_permalink(self):

        url = base_url + '/chat.getPermalink'

        body = self.client.SlackChat.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def share_chat_me_message(self):

        url = base_url + '/chat.meMessage'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def send_ephemeral_message(self):

        url = base_url + '/chat.postEphemeral'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def send_message(self):

        url = base_url + '/chat.postMessage'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def schedule_message(self):

        url = base_url + '/chat.scheduleMessage'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def custom_unfurl_behavior(self):

        url = base_url + '/chat.unfurl'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def update_message(self):

        url = base_url + '/chat.update'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_scheduled_messages(self):

        url = base_url + '/chat.scheduledMessages.list'

        body = self.client.SlackChat.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class SlackConversations(SlackClient):

    def __init__(self,client):
        self.client = client

    def archive_conversation(self):

        url = base_url + '/conversations.archive'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def close_message(self):

        url = base_url + '/conversations.close'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def initiate_conversation(self):

        url = base_url + '/conversations.create'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def fetch_conversation_history(self):

        url = base_url + '/conversations.history'

        body = self.client.SlackConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def retrieve_conversation_information(self):

        url = base_url + '/conversations.info'

        body = self.client.SlackConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def invite_user(self):

        url = base_url + '/conversations.invite'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def join_conversation(self):

        url = base_url + '/conversations.join'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def remove_conversation_user(self):

        url = base_url + '/conversations.kick'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def leave_conversation(self):

        url = base_url + '/conversations.leave'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_channels(self):

        url = base_url + '/conversations.list'

        body = self.client.SlackConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def set_read_cursor(self):

        url = base_url + '/conversations.mark'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def retrieve_conversation_members(self):

        url = base_url + '/conversations.members'

        body = self.client.SlackConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def open_or_resume_direct_message(self):

        url = base_url + '/conversations.open'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def rename_conversation(self):

        url = base_url + '/conversations.rename'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def retrieve_message_thread(self):

        url = base_url + '/conversations.replies'

        body = self.client.SlackConversations.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def set_conversation_purpose(self):

        url = base_url + '/conversations.setPurpose'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_topic(self):

        url = base_url + '/conversations.setTopic'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def unarchive_conversation(self):

        url = base_url + '/conversations.unarchive'

        body = self.client.SlackConversations.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

class SlackDialog(SlackClient):

    def __init__(self,client):
        self.client = client


    def open_dialog(self):

        url = base_url + '/dialog.open'

        body = self.client.SlackDialog.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class SlackDoNotDisturb(SlackClient):

    def __init__(self,client):
        self.client = client


    def end_user_snooze_mode(self):

        url = base_url + '/dnd.endSnooze'

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token))

        pprint(request)

    def retrieve_user_dnd_status(self):

        url = base_url + '/dnd.info'

        body = self.client.SlackDoNotDisturb.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def end_user_dnd_session(self):

        url = base_url + '/dnd.endDnd'

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token))

        pprint(request)

    def turn_on_dnd_session(self):

        url = base_url + '/dnd.setSnooze'

        body = self.client.SlackDoNotDisturb.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def retrieve_dnd_status(self):

        url = base_url + '/dnd.teamInfo'

        body = self.client.SlackDoNotDisturb.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class SlackFiles(SlackClient):

    def __init__(self,client):
        self.client = client


    def delete_existing_file_comment(self):

        url = base_url + '/files.comments.delete'

        body = self.client.SlackFiles.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def delete_file(self):

        url = base_url + '/files.delete'

        body = self.client.SlackFiles.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_file_info(self):

        url = base_url + '/files.info'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_team_files(self):

        url = base_url + '/files.list'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def revoke_file_sharing(self):

        url = base_url + '/files.revokePublicURL'

        body = self.client.SlackFiles.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def enable_file_sharing(self):

        url = base_url + '/files.sharedPublicURL'

        body = self.client.SlackFiles.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def upload_file(self):

        url = base_url + '/files.upload'

        body = self.client.SlackFiles.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def add_remote_file(self):

        url = base_url + '/files.remote.add'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_remote_file_info(self):

        url = base_url + '/files.remote.info'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_remote_files(self):

        url = base_url + '/files.remote.list'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def remove_remote_file(self):

        url = base_url + '/files.remote.remove'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def share_remote_file(self):

        url = base_url + '/files.remote.share'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def update_remote_file(self):

        url = base_url + '/files.remote.update'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def remote_file_search(self):

        url = base_url + '/search.files'

        body = self.client.SlackFiles.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

class SlackGroups(SlackClient):

    def __init__(self,client):
        self.client = client


    def archive_private_channel(self):

        url = base_url + '/groups.archive'

        body = self.client.SlackGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def create_private_channel(self):

        url = base_url + '/groups.create'

        body = self.client.SlackGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def clone_archive_private_channel(self):

        url = base_url + '/groups.createChild'

        body = self.client.SlackGroups.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class SlackMigration(SlackClient):

    def __init__(self,client):
        self.client = client

    def map_user_to_global(self):

        url = base_url + '/migration.exchange'

        body = self.client.SlackMigration.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class SlackOAuth(SlackClient):

    def __init__(self,client):
        self.client = client


    def exchange_code_for_access_token(self):

        url = base_url + '/oauth.access'

        body = self.client.SlackOAuth.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def exchange_code_for_workspace_token(self):

        url = base_url + '/oauth.token'

        body = self.client.SlackOAuth.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def exchange_code_for_access_token_v2(self):

        url = base_url + '/oauth.v2.access'

        body = self.client.SlackOAuth.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class SlackPins(SlackClient):

    def __init__(self,client):

        self.client = client

    def pin_item_to_channel(self):

        url = base_url + '/pins.add'

        body = self.client.SlackPins.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_pins(self):

        url = base_url + '/pins.list'

        body = self.client.SlackPins.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def unpin(self):

        url = base_url + '/pins.remove'

        body = self.client.SlackPins.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

class SlackReactions(SlackClient):

    def __init__(self,client):
        self.client = client


    def add_reaction(self):

        url = base_url + '/reactions.add'

        body = self.client.SlackReactions.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_reactions(self):

        url = base_url + '/reactions.get'

        body = self.client.SlackReactions.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_reactions(self):

        url = base_url + '/reactions.list'

        body = self.client.SlackReactions.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def remove_reaction(self):

        url = base_url + '/reactions.remove'

        body = self.client.SlackReactions.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

class SlackReminders(SlackClient):

    def __init__(self,client):
        self.client = client


    def create_reminder(self):

        url = base_url + '/reminders.add'

        body = self.client.SlackReminders.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def mark_reminder_complete(self):

        url = base_url + '/reminders.complete'

        body = self.client.SlackReminders.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def delete_reminder(self):

        url = base_url + '/reminders.delete'

        body = self.client.SlackReminders.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_reminder_info(self):

        url = base_url + '/reminders.info'

        body = self.client.SlackReminders.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_reminders(self):

        url = base_url + '/reminders.list'

        body = self.client.SlackReminders.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class SlackRTM(SlackClient):

    def __init__(self,client):

        self.client = client


    def start_rtm_session_connect(self):

        url = base_url + '/rtm.connect'

        body = self.client.SlackRTM.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def start_rtm_session_start(self):

        url = base_url + '/rtm.start'

        body = self.client.SlackRTM.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class SlackSearch(SlackClient):

    def __init_(self,client):

        self.client = client

    def file_search(self):

        url = base_url + '/search.files'

        body = self.client.SlackSearch.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def message_search(self):

        url = base_url + '/search.messages'

        body = self.client.SlackSearch.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)


class SlackStars(SlackClient):

    def __init__(self,client):

        self.client = client


    def add_star(self):

        url = base_url + '/stars.add'

        body = self.client.SlackStars.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_user_stars(self):

        url = base_url + '/stars.list'

        body = self.client.SlackStars.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def remove_star(self):

        url = base_url + '/stars.remove'

        body = self.client.SlackStars.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

class SlackTeam(SlackClient):

    def __init__(self,client):
         self.client = client


    def get_team_access_logs(self):

        url = base_url + '/team.accessLogs'

        body = self.client.SlackTeam.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_billable_team_members(self):

        url = base_url + '/team.billableInfo'

        body = self.client.SlackTeam.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_team_information(self):

        url = base_url + '/team.info'

        body = self.client.SlackTeam.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_team_integration_logs(self):

        url = base_url + '/team.integrationLogs'

        body = self.client.SlackTeam.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_teams_profile(self):

        url = base_url + '/team.profile.get'

        body = self.client.SlackTeam.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

class SlackUserGroups(SlackClient):

    def __init__(self,client):

        self.client = client


    def creat_user_group(self):

        url = base_url + "/usergroups.create"

        body = self.client.SlackUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def disable_user_group(self):

        url = base_url + '/usergroups.disable'

        body = self.client.SlackUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def enable_user_group(self):

        url = base_url + '/usergroups.enable'

        body = self.client.SlackUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_all_team_user_groups(self):

        url = base_url + '/usergroups.list'

        body = self.client.SlackUserGroups.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def update_user_group(self):

        url = base_url + '/usergroups.update'

        body = self.client.SlackUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def list_usergroup_users(self):

        url = base_url + '/usergroups.users.list'

        body = self.client.SlackUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def update_usergroup_users(self):

        url = base_url + '/usergroups.users.update'

        body = self.client.SlackUserGroups.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class SlackUsers(SlackClient):

    def __init__(self,client):
        self.client = client

    def list_user_conversations(self):

        url = base_url + '/users.conversations'

        body = self.client.SlackUsers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def delete_profile_picture(self):

        url = base_url + '/users.deletePhoto'

        body = self.client.SlackUsers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_user_presence_info(self):

        url = base_url + '/users.getPresence'

        body = self.client.SlackUsers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_user_identity(self):

        url = base_url + '/users.identity'

        body = self.client.SlackUsers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def get_user_info(self):

        url = base_url + '/users.info'

        body = self.client.SlackUsers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def list_all_team_users(self):

        url = base_url + '/users.list'

        body = self.client.SlackUsers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def find_user_via_email(self):

        url = base_url + '/users.lookupByEmail'

        body = self.client.SlackUsers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def mark_user_active(self):

        url = base_url + '/users.setActive'

        body = self.client.SlackUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_user_profile_photo(self):

        url = base_url + '/users.setPhoto'

        body = self.client.SlackUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def set_user_presence(self):

        url = base_url + '/users.setPresence'

        body = self.client.SlackUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def get_user_profile_info(self):

        url = base_url + '/users.profile.get'

        body = self.client.SlackUsers.generate_queries()

        request = requests.get(url,auth=HTTPBasicAuth('',self.client.token),params=body)

        pprint(request)

    def set_user_profile_info(self):

        url = base_url + '/users.profile.set'

        body = self.client.SlackUsers.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)


class SlackViews(SlackClient):

    def __init__(self,client):

        self.client = client


    def open_user_view(self):

        url = base_url + '/views.open'

        body = self.client.SlackViews.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def publish_static_user_view(self):

        url = base_url + '/views.publish'

        body = self.client.SlackViews.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def push_root_view(self):

        url = base_url + '/views.push'

        body = self.client.SlackViews.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def update_existing_view(self):

        url = base_url + '/views.update'

        body = self.client.SlackViews.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

class SlackWorkflows(SlackClient):

    def __init__(self,client):

        self.client = client

    def indicate_workflow_complete(self):

        url = base_url + '/workflows.stepCompleted'

        body = self.client.SlackWorkflows.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def indicate_workflow_failed(self):

        url = base_url + '/workflows.stepFailed'

        body = self.client.SlackWorkflows.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)

    def update_workflow_step_config(self):

        url = base_url + '/workflows.updateStep'

        body = self.client.SlackWorkflows.generate_queries()

        request = requests.post(url,auth=HTTPBasicAuth('',self.client.token),json=body)

        pprint(request)



































def main():

    client = SlackClient('636558213122.2172017410279')
    oauthRequests = OauthMethods(client)
    oauthRequests.scopes.append('incoming-webhook')
    oauthRequests.scopes.append('commands')
    oauthRequests.generate_redirect()


if __name__ == '__main__':
    main()