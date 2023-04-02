import discord #https://discordpy.readthedocs.io/en/stable/
import os
import chat_response
import Console_Text
import requests
from weather_report import get_weather

from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv #https://pypi.org/project/python-dotenv/

intents = discord.Intents.default() #https://discordpy.readthedocs.io/en/stable/intents.html
intents.message_content = True
#TODO determine what intents are needed
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all()) #https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html
user  = False
sched = False

@bot.event
async def on_ready(): #https://superfastpython.com/asyncio-async-def/
    print(Console_Text.Get_Time(), 'Logged in as:',bot.user.name)
    print("ID:",bot.user.id)
    print('-----------------------------------------')

@tasks.loop(minutes = 180)
async def on_schedule():
    message = get_weather()
    print(Console_Text.Get_Time(), "Weather Report") #makes note in terminal
    await user.channel.send(message)

    
@bot.event
async def on_message(message): 
    global sched
    global user
    if sched == False:
        user = message
        on_schedule.start()
        sched = True

    if (message.author.bot or (chat_response.Check_Intent(message) == False)):
        return
    else:
        await message.channel.send(chat_response.check_contents(message))




load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
