import discord
import os


def check_contents(message):                              #TODO possibly change to switch statement for readabilty  
    if message.content.startswith('$'):
       reply = check_verbage(message)
       return reply
    else: return #prevents error 400 bad request in terminal

def check_verbage(message):
    if message.content.__contains__('hey'):
        text = "Hi everybody! ＼(^o^)／"
        print("Said hi") #makes note in terminal
    return text
