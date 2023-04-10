import discord
import os
import Console_Text
import asyncio
from weather_report import get_weather
import requests
import TwitchAuth
import webbrowser
from urllib.parse import urlparse, parse_qs
import json

client_secret = '5nc2a3uhs3orwxp5dsbjxztjhqbomb'
grant_type = 'client_credentials'


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
        url = "https://id.twitch.tv/oauth2/authorize" \
              "?response_type=code" \
              "&client_id=l9lwpc7k4zsmu2mphiuku5thumguht" \
              "&redirect_uri=https://discord.com/api/webhooks/1094773478445563964/oRp8vFAasyPVjNdWxvDVbk4tQlNK97s5L_MUfYXGslffyzPtWPSpV62fXmR0a_k71O6n" \
              "&scope=user:read:follows"
        webbrowser.open(url)
        response = requests.get('https://discord.com/api/webhooks/1094773478445563964/oRp8vFAasyPVjNdWxvDVbk4tQlNK97s5L_MUfYXGslffyzPtWPSpV62fXmR0a_k71O6n')
        print(response.status_code)
        print(response.text)
        print(Console_Text.Get_Time(), "twitch-connect command") #makes note in terminal

        json_response = json.loads(response.text)
        token = json_response['token']
        print(token)

    elif message.content.__contains__('twitch'):
        text = "Twitch Commands:" \
               "\n--------------------------------------------" \
               "\ntwitch-list -> List current notification sources" \
               "\ntwitch-live -> List current live streamers" \
               "\ntwitch-add 'source' -> Add notification source" \
               "\ntwitch-delete 'source' -> Delete notification source" \
               "\ntwitch-edit 'source' -> Edit notification source" \
               "\ntwitch-connect -> Connect to your Twitch account" 
        print(Console_Text.Get_Time(), "Twitch command")  # makes note in terminal
    return text

