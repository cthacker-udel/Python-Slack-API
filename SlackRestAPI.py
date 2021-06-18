from SlackClient import SlackClient
import requests
from pprint import pprint
import urllib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from selenium_stealth import stealth
import time


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




def main():

    client = SlackClient('636558213122.2172017410279')
    oauthRequests = OauthMethods(client)
    oauthRequests.scopes.append('incoming-webhook')
    oauthRequests.scopes.append('commands')
    oauthRequests.generate_redirect()


if __name__ == '__main__':
    main()