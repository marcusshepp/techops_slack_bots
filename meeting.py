from slackclient import SlackClient

from token import TOKEN

dev_channel = "C02RXLYLG"
dev = "#dev"
user = "USLACKBOT"
message = "Excuse me, sorry to interupt.\nMeeting starts in ten minutes."
sc = SlackClient(TOKEN)
print sc.api_call("chat.postMessage", as_user="false", channel=dev, text=message, username="Gentle Meeting Reminder", icon_emoji=":panda_face:")
