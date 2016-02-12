from slackclient import SlackClient

from token import TOKEN

dev_channel = "C02RXLYLG"
dev = "#dev"
user = "USLACKBOT"
message = "HAPPY MERGE DAY\nLet's review it up!"
sc = SlackClient(TOKEN)
print sc.api_call("chat.postMessage", as_user="false", channel=dev, text=message, username="Merge Day Bot", icon_emoji=":merged:")
