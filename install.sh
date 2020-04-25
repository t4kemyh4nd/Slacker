#!/bin/bash

echo "Installing Slacker..."

pip install -r requirements.txt

read -p "Enter facebook app ID: " FB_APP_ID
read -p "Enter facebook access token: " FB_ACCESS_TOKEN
read -p "Enter Slack bot token: " SLACK_BOT_TOKEN
read -p "Enter Slack webhook URL: " SLACK_WEBHOOK_URL

echo "export FB_APP_ID='$FB_APP_ID'" >> ~/.bashrc
echo "export FB_APP_ID='$FB_APP_ID'" >> ~/.profile
echo "FB_APP_ID='$FB_APP_ID'" >> /etc/enviroment

echo "export FB_ACCESS_TOKEN='$FB_ACCESS_TOKEN'" >> ~/.bashrc
echo "export FB_ACCESS_TOKEN='$FB_ACCESS_TOKEN'" >> ~/.profile
echo "FB_ACCESS_TOKEN='$FB_ACCESS_TOKEN'" >> /etc/environment

echo "export SLACK_WEBHOOK_URL='$SLACK_WEBHOOK_URL'" >> ~/.bashrc
echo "export SLACK_WEBHOOK_URL='$SLACK_WEBHOOK_URL'" >> ~/.profile
echo "SLACK_WEBHOOK_URL='$SLACK_WEBHOOK_URL'" >> /etc/environment

echo "export SLACK_BOT_TOKEN='$SLACK_BOT_TOKEN'" >> ~/.bashrc
echo "export SLACK_BOT_TOKEN='$SLACK_BOT_TOKEN'" >> ~/.profile
echo "SLACK_BOT_TOKEN='$SLACK_BOT_TOKEN'" >> /etc/environment

source ~/.bashrc
source ~/.profile
