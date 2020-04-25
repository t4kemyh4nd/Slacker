#!/bin/bash

echo "Installing Slacker..."

pip install -r requirements.txt

read -p "Enter facebook app ID: " FB_APP_ID
read -p "Enter facebook access token: " FB_ACCESS_TOKEN
read -p "Enter Slack bot token: " SLACK_BOT_TOKEN
read -p "Enter Slack webhook URL: " SLACK_WEBHOOK_URL
read -p "Enter full path of dirsearch python file (eg. /users/dirsearch/dirsearch.py): " DIRSEARCH_PATH

echo "{\"FB_APP_ID\": \"$FB_APP_ID\", \"FB_ACCESS_TOKEN\": \"$FB_ACCESS_TOKEN\", \"SLACK_BOT_TOKEN\": \"$SLACK_BOT_TOKEN\", \"SLACK_WEBHOOK_URL\": \"$SLACK_WEBHOOK_URL\", \"DIRSEARCH_PATH\": \"$DIRSEARCH_PATH\"}" > ./recon-bot/config.json

echo "Done..."
