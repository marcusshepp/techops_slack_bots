import requests, time
from slackclient import SlackClient

from token import TOKEN
from bots import RespondBot

TEST_CHANNEL = "C0M5VFD2Q"
RANDOM_CHANNEL = "C02GE2V9U"
SC = SlackClient(TOKEN)



class WeatherBot(RespondBot):
    
    def __init__(self, **kw):
        super(WeatherBot, self).__init__(**kw)
    
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

if __name__ == '__main__':
    tr = {
        "weather summary": "Current Brief Weather Summary: {}".format(weather_summary()),
        "temperature": "Current Temperature: {} Degrees Ferienheit".format(temp()),
        "temp": "Current Temperature: {} Degrees Ferienheit".format(temp()),
        "wind speed": "Current Wind Speed: {} MPH".format(wind_mph())}

    bot_data = {
        "username": "Weather Bot",
        "icon": ":mostly_sunny:",
        "channels": "*",
        "triggers_responses": tr}
    wb = WeatherBot(**bot_data)
    wb.listen()
