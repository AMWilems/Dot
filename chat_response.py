import discord
import os
import Console_Text
import asyncio
from weather_report import get_weather
import requests
import Twitch
import webbrowser
from urllib.parse import urlparse, parse_qs
import json

def Check_Intent(message):
    if message.content.startswith('$'):
        return True
    else:
        return False #prevents error 400 bad request in terminal

def check_contents(message):
    reply = check_verbage(message)
    return reply


def check_verbage(message):
    if message.content.__contains__('hey'):
        text = "Hi everybody! ＼(^o^)／"
        print(Console_Text.Get_Time(), "Said hi") #makes note in terminal
    elif message.content.__contains__('weather'):
        text = get_weather()
        res = requests.get(get_weather())
        print(Console_Text.Get_Time(), "Weather Report") #makes note in terminal
    elif message.content.__contains__('twitch-connect'):
        text = "Obtaining user access token..."
        twitch_api = Twitch.Twitch()
        twitch_api.authorize_user_token()
        username = remove_prefix(message.content, prefix="$twitch-connect ")
        print(username)
    elif message.content.__contains__('twitch-get-channel-emotes'):
        text = "List emotes here..."
        broadcaster_id = remove_prefix(message.content, prefix="$twitch-get-channel-emotes ")
        print(broadcaster_id)
    elif message.content.__contains__('twitch'):
        text = "Twitch Commands:" \
               "\n--------------------------------------------" \
               "\ntwitch-connect 'your_twitch_username' -> Connect to your Twitch account" \
               "\ntwitch-get-channel-emotes 'Broadcaster ID' -> List a Channel's Custom Emotes"
        print(Console_Text.Get_Time(), "Twitch command")  # makes note in terminal
    return text

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text
