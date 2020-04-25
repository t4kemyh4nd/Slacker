#!/bin/bash

echo "Installing Slacker..."

pip install -r requirements.txt

read -p "Enter facebook app ID" FB_APP_ID
read -p "Enter facebook access token" FB_ACCESS_TOKEN
read -p "Enter Slack bot token" SLACK_BOT_TOKEN
read -p "Enter Slack webhook URL" SLACK_WEBHOOK_URL

function addVar() {
echo "Adding $1 to env variables..."
echo $1 >> ~/.bashrc
echo $1 >> ~/.profile
echo $1 >> /etc/environment
echo "Done..."
}

addVar $FB_APP_ID
addVar $FB_ACCESS_TOKEN
addVar $SLACK_BOT_TOKEN
addVar $SLACK_WEBHOOK_URL

source ~/.bashrc
source ~/.profile
