import discord #https://discordpy.readthedocs.io/en/stable/
import os
import chat_response
import Console_Text

from discord.ext import commands
from dotenv import load_dotenv #https://pypi.org/project/python-dotenv/

intents = discord.Intents.default() #https://discordpy.readthedocs.io/en/stable/intents.html
intents.message_content = True
#TODO determine what intents are needed
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all()) #https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html

@bot.event
async def on_ready(): #https://superfastpython.com/asyncio-async-def/
    print(Console_Text.GetTime(), 'Logged in as:',bot.user.name)
    print("ID:",bot.user.id)
    print('-----------------------------------------')
    
@bot.event
async def on_message(message):
    if (message.author.bot or (check_contents(message) == False)):
        return
    else:
        await message.channel.send(chat_response.check_contents(message))

    
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
