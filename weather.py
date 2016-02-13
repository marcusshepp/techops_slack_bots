import requests, time
from slackclient import SlackClient

from token import TOKEN

TEST_CHANNEL = "C0M5VFD2Q"
RANDOM_CHANNEL = "C02GE2V9U"
SC = SlackClient(TOKEN)

def handle(text):
    print text
    if text:
        message = text[0].get("text", None)
        channel = text[0].get("channel", None)
        if message == "temp" or message == "temperature":
            current_temp = temp()
            message = "The current temperature is: {}".format(current_temp)
            SC.api_call("chat.postMessage", as_user="false", channel=channel, text=message, username="Weather Bot", icon_emoji=":mostly_sunny:")
        elif message == "weather summary":
            summary = weather_summary()
            message = "Breif Weather Summary: {}".format(summary)
            SC.api_call("chat.postMessage", as_user="false", channel=channel, text=message, username="Weather Bot", icon_emoji=":mostly_sunny:")
    # print type(text)

def listen():
    if SC.rtm_connect():
        while True:
            handle(SC.rtm_read())
            time.sleep(1)

def hit_weather():
    api_key = "614d199c734be239950bc890c7f30e9d"
    lat_long = (43.5978070,-84.7675140)
    url = "https://api.forecast.io/forecast/{APIKEY}/{LATITUDE},{LONGITUDE}".format(APIKEY=api_key, LATITUDE=lat_long[0], LONGITUDE=lat_long[1])
    r = requests.get(url)
    return r.json()

def temp():
    j = hit_weather()
    return j["currently"]["temperature"]

def weather_summary():
    j = hit_weather()
    print j["currently"]
    return j["currently"]["summary"]

listen()
