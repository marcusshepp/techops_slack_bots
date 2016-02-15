import requests, time
from slackclient import SlackClient

from token import TOKEN

TEST_CHANNEL = "C0M5VFD2Q"
RANDOM_CHANNEL = "C02GE2V9U"
SC = SlackClient(TOKEN)

class Bot(object):
    def __init__(self, username="", icon="", channels=""):
        self.icon = icon
        self.channels = channels
        self.username = username

class RespondBot(Bot):

    def __init__(self, triggers_responses, **kw):
        super(RespondBot, self).__init__(**kw)
        self.triggers_responses = triggers_responses

    def say(self, channel, message):
        SC.api_call("chat.postMessage", as_user="false", channel=channel, text=message, username=self.username, icon_emoji=self.icon)

    def listen(self):
        if SC.rtm_connect():
            while True:
                sc = SC.rtm_read()
                if sc:
                    self.handle(sc[0])
                time.sleep(1)

    def handle(self, text):
        for k, v in self.triggers_responses.items():
            t = text.get("text", None)
            if t:
                if k in text["text"]:
                    self.say(text["channel"], v)

"""
tr = {"qwe": ":smile:"}

data = {
    "username": "notabot",
    "icon": ":poop:",
    "channels": "*",
    "triggers_responses": tr
}

rb = RespondBot(**data)
rb.listen()
"""
