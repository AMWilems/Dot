#pip install youtube_dl
import yt_dlp as youtube_dl
import discord
import asyncio

youtube_dl.utils.bug_reports_message = lambda: ''

format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # I think this needs changed?
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(format_options)

class MusicSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.25):
        super().__init(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url= ""

    #takes in url as a parameter, downloads the relevant file, and returns the filename
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):

        #allows download of file in background while performing other bot tasks
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        #if url points to a playlist, take the first video in playlist
        if 'entries' in data:
            data = data['entries'][0]

        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename
