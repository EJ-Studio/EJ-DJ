import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from packages.CRITICAL.CLIENT import client
from commands.data import FOOTER, BOT_CHANNELS

@client.command(pass_context=True, aliases=["Resume"])
async def resume(ctx):
	if ctx.channel.name in BOT_CHANNELS.channels:

		voice = get(client.voice_clients, guild=ctx.guild)

		if voice.is_playing():
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="",
				description=f"Music is already playing")
			update = await ctx.send(embed = update_embed)
			return
		else:
			update_embed = discord.Embed(
				colour=discord.Colour.green(),
				title="",
				description=f"Resuming music")
			update = await ctx.send(embed = update_embed)
			voice.resume()
			return