import discord
import youtube_dl
import os
#import ffprobe
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from packages.CRITICAL.CLIENT import client
from commands.data import FOOTER, BOT_CHANNELS

@client.command(pass_context=True)
async def stop(ctx):#, url):
	if ctx.channel.name in BOT_CHANNELS.channels:

		voice = get(client.voice_clients, guild=ctx.guild)

		voice.stop()