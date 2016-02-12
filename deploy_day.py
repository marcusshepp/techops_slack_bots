from slackclient import SlackClient

from token import TOKEN

dev_channel = "C02RXLYLG"
dev = "#dev"
user = "USLACKBOT"
message = "HAPPY DEPLOY DAY\nLet's get this code off the ground!"
sc = SlackClient(TOKEN)
print sc.api_call("chat.postMessage", as_user="false", channel=dev, text=message, username="Deploy Day Bot", icon_emoji=":rocket:")
