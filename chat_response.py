import discord
import os
import Console_Text
import asyncio
from weather_report import get_weather
import requests


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
    return text

