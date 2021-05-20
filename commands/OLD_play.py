import discord
import youtube_dl
import os
#import ffprobe
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from packages.CRITICAL.CLIENT import client

@client.command(pass_context=True, aliases=['p', 'Play'])
async def play(ctx, url: str):
  song_there = os.path.isfile("song.mp3")
  try:
    if song_there:
      os.remove("song.mp3")
  except PermissionError:
    await ctx.send("Wait for the current playing music end or use the 'stop' command")
    return
  await ctx.send("Getting everything ready, playing audio soon")
  print("Someone wants to play music let me get that ready for them...")
  voice = get(client.voice_clients, guild=ctx.guild)
  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
    }],
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      os.rename(file, 'song.mp3')
  try:
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
  except Exception as Error:
    await ctx.send("Please retry that.")
  voice.volume = 100
  voice.is_playing()


#OLD CODE MIGHT COME IN HANDY SOON!!!!
  # players = {}
  # server = ctx.message.guild
  # voice_client = ctx.voice_client_in(server)
  # player = await voice_client.create_ytdl_player(url)
  # players[server.id] = player
  # player.start()
  ###await ctx.voice_client.create_ytdl_player(url)
  #await VoiceClient.play("audio.mp3")





#   @bot.command(pass_context=True, brief="This will play a song 'play [url]'", aliases=['pl'])
#async def play(ctx, url: str):