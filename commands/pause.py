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

@client.command(pass_context=True, aliases=["Pause"])
async def pause(ctx):#, url):
	if ctx.channel.name in BOT_CHANNELS.channels:
		try:
			voice = get(client.voice_clients, guild=ctx.guild)
			if voice.is_playing():
				update_embed = discord.Embed(
					colour=discord.Colour.green(),
					title="",
					description=f"Paused music")
				update = await ctx.send(embed = update_embed)
				voice.pause()
				return
			else:
				if voice.is_paused():
					update_embed = discord.Embed(
						colour=discord.Colour.gold(),
						title="",
						description=f"Music is already paused")
					update = await ctx.send(embed = update_embed)
					return
				else:
					update_embed = discord.Embed(
						colour=discord.Colour.gold(),
						title="",
						description=f"Not playing any music")
					update = await ctx.send(embed = update_embed)
					return
		except:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="",
				description=f"Their is no music playing")
			update = await ctx.send(embed = update_embed)