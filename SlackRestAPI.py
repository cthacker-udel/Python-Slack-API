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
















def main():

    client = SlackClient('636558213122.2172017410279')
    oauthRequests = OauthMethods(client)
    oauthRequests.scopes.append('incoming-webhook')
    oauthRequests.scopes.append('commands')
    oauthRequests.generate_redirect()


if __name__ == '__main__':
    main()