import requests
import json

webhook_url = "https://hooks.slack.com/services/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"


def send_to_channel(channel, location, username):
    """
    Posts a message to slack.
    """
    text = "{} wants you to know that there is free food \
    in the {}".format(username,
                      location
                      )
    payload = {
                "channel":   channel,
                "text":      text
            }
    r = requests.post(webhook_url, data=json.dumps(payload))
    if r.status_code == 200:
        return True
    return False
