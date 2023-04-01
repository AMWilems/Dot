import discord #https://discordpy.readthedocs.io/en/stable/
import os
import chat_response
import Console_Text
from Music_Util import MusicSource

from discord.ext import commands
from dotenv import load_dotenv #https://pypi.org/project/python-dotenv/

intents = discord.Intents.default() #https://discordpy.readthedocs.io/en/stable/intents.html
intents.message_content = True
#TODO determine what intents are needed
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all()) #https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html

@bot.event
async def on_ready(): #https://superfastpython.com/asyncio-async-def/
    print(Console_Text.Get_Time(), 'Logged in as:',bot.user.name)
    print("ID:",bot.user.id)
    print('-----------------------------------------')

@bot.event
async def on_message(message):
    #without this line, commands won't work (it takes all chat messages and passes them into on_message)
    await bot.process_commands(message)
    if (message.author.bot or (chat_response.Check_Intent(message) == False)):
        return
    else:
        await message.channel.send(chat_response.check_contents(message))
        

#joins voice channel with the user that called the function
@bot.command(name='join', help='Tells bot to join voice channel')
async def join(ctx):
    #check if user is in a voice channel
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    #join channel
    await channel.connect()

@bot.command(name='leave', help='Tells bot to leave voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    #executes if bot is currently in a voice channel
    if voice_client.is_connected():
        await voice_client.disconnect()
    #executes if bot is not currently in a voice channel
    else:
        await ctx.send("Dot is not currently in a voice channel.")

@bot.command(name='play', help='To play song')
async def play(ctx,url):
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await MusicSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='pause', help='Pauses song')
async def pause(ctx):
    vc = ctx.message.guild.voice_client
    if vc.is_playing():
        vc.pause()
    else:
        await ctx.send("Lmao can't pause what isn't playing")

@bot.command(name='resume')
async def resume(ctx):
    vc = ctx.message.guild.voice_client
    if vc.is_paused():
        vc.resume()
    else:
        await ctx.send("Can't unpause what wasn't paused, dummy")

@bot.command(name='stop')
async def stop(ctx):
    vc = ctx.message.guild.voice_client
    if vc.is_paused() or vc.is_playing():
        vc.stop()
    else:
        await ctx.send("Can't stop if we never started")

    
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
