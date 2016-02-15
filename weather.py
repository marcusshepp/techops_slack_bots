import requests, time
from slackclient import SlackClient

from token import TOKEN
from bots import RespondBot

TEST_CHANNEL = "C0M5VFD2Q"
RANDOM_CHANNEL = "C02GE2V9U"
SC = SlackClient(TOKEN)
bot_data = {
    "username": "Weather Bot"}
rs = RespondBot

def handle(text):
    nt = text
    print nt
    if nt:
        message = nt[0].get("text", None)
        channel = nt[0].get("channel", None)
        if message == "temp" or message == "temperature":
            current_temp = temp()
            message = "The current temperature is: {} degrees ferienheit.".format(current_temp)
            say(channel, message)
        elif message == "weather summary":
            summary = weather_summary()
            message = "Breif Weather Summary: {}".format(summary)
            say(channel, message)
        elif message == "wind speed":
            mph = wind_mph()
            message = "Current Wind Speed: {} MPH".format(mph)
            say(channel, message)

def listen():
    if SC.rtm_connect():
        while True:
            sc = SC.rtm_read()
            if sc:
                handle(sc)
            time.sleep(1)

def say(channel, message):
    SC.api_call("chat.postMessage", as_user="false", channel=channel, text=message, username="Weather Bot", icon_emoji=":mostly_sunny:")

def hit_weather():
    api_key = "614d199c734be239950bc890c7f30e9d"
    lat_long = (43.5978070,-84.7675140)
    url = "https://api.forecast.io/forecast/{APIKEY}/{LATITUDE},{LONGITUDE}".format(APIKEY=api_key, LATITUDE=lat_long[0], LONGITUDE=lat_long[1])
    r = requests.get(url)
    return r.json()

def curr(s):
    j = hit_weather()
    return j["currently"][s]

def temp():
    return curr("temperature")

def weather_summary():
    return curr("summary")

def wind_mph():
    return curr("windSpeed")

def p():
    return hit_weather()

if __name__ == '__main__':
    handle(listen())
    # p = p()
    # for i in p:
        # print i
        # time.sleep(1)
    # print p["currently"]
