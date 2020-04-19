import requests
import json
import os
from datetime import datetime
from OpenSSL import crypto
import random

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

    def checkNewCert(self, domain):
        try:
            today = datetime.today().strftime('%Y-%m-%d')
            payload = {'query': domain, 'fields': 'not_valid_before', 'access_token': self.access_token}
            response = json.loads(requests.get("https://graph.facebook.com/v6.0/certificates", params = payload).text)
            for date in response['data']:
                print(date['not_valid_before'].split("T")[0])
        except:
            print("Error in getting new certificates")

    @staticmethod
    def readDomainFromCert(cert):
        filename = 'test' + str(random.randrange(20, 50, 1)) + '.pem'
        file = open(filename, 'w')
        for line in cert.splitlines():
            file.write(line.strip())
        file.close()
        cert_file = filename
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
        subject = cert.get_subject()
        issued_to = subject.CN
        return issued_to