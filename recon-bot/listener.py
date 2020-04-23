from slacker import Slacker
from flask import Flask, request, abort
from ctapi import Alerter
import os
import dirapi
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["dirscan"]
col = db["domains"]

#define slack api token and fb access token here
slack = Slacker(os.environ["SLACK_BOT_TOKEN"])
alerter = Alerter(os.environ["FB_ACCESS_TOKEN"], '666434090858702')

app = Flask(__name__)

@app.route('/list-domains', methods=['POST'])
def list():
    if request.method == 'POST':
        domains = alerter.listDomains()
        slack.chat.post_message('#subdomain-alerts', "List of subscribed domains")
        for domain in domains:
            slack.chat.post_message('#subdomain-alerts', domain['domain'])
        return '', 200

@app.route('/add-domain', methods=['POST'])
def add():
    if request.method == 'POST':
        response = alerter.addDomain(request.form['text'])
        if response is True:
            slack.chat.post_message('#subdomain-alerts', "Successfully added " + request.form['text'])
            return '', 200
        else:
            slack.chat.post_message('#subdomain-alerts', "Could not add " + request.form['text'])
            return 'Error', 200
    else:
        print("Failed")

@app.route('/remove-domain', methods=['POST'])
def remove():
    if request.method == 'POST':
        response = alerter.removeDomain(request.form['text'])
        if response is True:
            slack.chat.post_message('#subdomain-alerts', "Successfully removed " + request.form['text'])
            return '', 200
        else:
            slack.chat.post_message('#subdomain-alerts', "Could not remove " + request.form['text'])
            return 'Error', 200
    else:
        print("Failed")

@app.route('/subdomain-alert', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        print(request.get_json())
        if "certificate" in request.get_json()["entry"][0]["changes"][0]["field"]:
            domain = Alerter.readDomainFromCert(request.get_json()["entry"][0]["changes"][0]["value"]["certificate_pem"])
            slack.chat.post_message('#subdomain-alerts', "New certificate added for " + domain)
            return '', 200
    elif request.method == 'GET':
        return str(request.args['hub.challenge']), 200

@app.route('/add-dirscan', methods=['POST'])
def addDirscan():
    if request.method == 'POST':
        try:
            domain = str()
            for x in col.find({"domain": request.form['text']}, {"domain": 1}):
                domain = x['domain']
            if not domain:
                slack.chat.post_message('#dirscan-alerts', "Added " + request.form['text'] + " for directory monitoring")
                return '', 200
                print(request.form['text'])
                dirapi.DirAlert(request.form['text'])
            else:
                slack.chat.post_message('#dirscan-alerts', "Already added " + request.form['text'] + " for directory monitoring")
                return '', 200
        except:
            slack.chat.post_message('#dirscan-alerts', "Couldn't add " + request.form['text'] + " for directory monitoring")
            return '', 200
    else:
        print("Failed")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)