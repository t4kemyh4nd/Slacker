import requests
import json

class Alerter:
    def __init__(self, access_token, app_id):
        self.access_token = access_token
        self.app_id = app_id

    def addDomain(self, domain):
        try:
            payload = {'subscribe': str(domain), 'access_token': self.access_token}
            response = json.loads(requests.post("https://graph.facebook.com/" + self.app_id + "/subscribed_domains", data = payload).text)
            if response['success'] == True:
                return True
        except:
            return response

    def listDomains(self):
        try:
            payload = {'fields': 'domain', 'access_token': self.access_token}
            response = json.loads(requests.get("https://graph.facebook.com/" + self.app_id + "/subscribed_domains", params = payload).text)
            return response['data']
        except:
            print("Error in listing subscribed domains")

    def removeDomain(self, domain):
        try:
            payload = {'unsubscribe': str(domain), 'access_token': self.access_token}
            response = json.loads(requests.post("https://graph.facebook.com/" + self.app_id + "/subscribed_domains", data = payload).text)
            if response['success'] == True:
                return True
        except:
            return response