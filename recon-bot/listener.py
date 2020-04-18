from slacker import Slacker
from flask import Flask, request, abort
from ctapi import Alerter

#define slack api token and fb access token here
slack = Slacker('xoxb-1069747671397-1069754474277-85D873Dili8hcATNVnRo9ic0')
alerter = Alerter('666434090858702|Ypbru4ktL06iaUTYBf4_lwC99VQ', '666434090858702')

app = Flask(__name__)

@app.route('/add-domain', methods=['POST'])
def add():
    if request.method == 'POST':
        domain = request.args['text']
        res = alerter.addDomain(domain)
        if res == True:
            slack.chat.post_message('#subdomain-alerts', "Successfully added " + domain)
        else:
            slack.chat.post_message('#subdomain-alerts', "Could not add " + domain)

@app.route('/list-domains', methods=['POST'])
def list():
    if request.method == 'POST':
        slack.chat.post_message('#subdomain-alerts', "List of subdomains: " + alerter.listDomains())

@app.route('/subdomain-alert', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return str(request.args['hub.challenge']), 200
    elif request.method == 'POST':
        print(request.json[''])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)