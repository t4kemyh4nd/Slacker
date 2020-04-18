from slacker import Slacker
from flask import Flask, request, abort
from ctapi import Alerter
import os

#define slack api token and fb access token here
slack = Slacker(os.environ["SLACK_BOT_TOKEN"])
alerter = Alerter(os.environ["FB_ACCESS_TOKEN"], '666434090858702')

app = Flask(__name__)

@app.route('/add-domain', methods=['POST'])
def add():
    if request.method == 'POST':
        domain = request.args['text']
        print(domain)
        response = alerter.addDomain(domain)
        if response == True:
            slack.chat.post_message('#subdomain-alerts', "Successfully added " + domain)
        else:
            slack.chat.post_message('#subdomain-alerts', "Could not add " + domain)
        return response, 200
    else:
        print("Failed")

@app.route('/list-domains', methods=['POST'])
def list():
    if request.method == 'POST':
        domains = alerter.listDomains()
        for domain in domains:
            slack.chat.post_message('#subdomain-alerts', domain['domain'])
        return '', 200

@app.route('/subdomain-alert', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return str(request.args['hub.challenge']), 200
    elif request.method == 'POST':
        print(request.json[''])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)