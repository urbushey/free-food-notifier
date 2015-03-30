import requests
import json

webhook_url = "https://hooks.slack.com/services/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"


def send_to_channel(channel, text):
    """
    Posts a message to slack.
    """
    payload = {
                "channel":   channel,
                "text":      text
            }
    r = requests.post(webhook_url, data=json.dumps(payload))
    return r
