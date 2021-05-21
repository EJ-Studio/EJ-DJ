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

client.remove_command('volume')
@client.command(pass_context=True, aliases=['v', 'Volume'])
async def volume(ctx, number: int):
	if ctx.channel.name in BOT_CHANNELS.channels:
		try:
			source = ctx.guild.voice_client.source

			# if not isinstance(source, discord.PCMVolumeTransformer):
			# 	update_embed = discord.Embed(
			# 		colour=discord.Colour.green(),
			# 		title="",
			# 		description=f"This source doesn't support adjusting volume or the interface to do so is not exposed.")
			# 	await ctx.send(embed = update_embed)
			# 	return


			# else:
			voice = get(client.voice_clients, guild=ctx.guild)
			number = int(number)/100

			voice.setVolume(0.5)
			#voice.volume = number

			update_embed = discord.Embed(
				colour=discord.Colour.green(),
				title="",
				description=f"Set the volume to {number}")
			await ctx.send(embed = update_embed)
			return

		except Exception as Error:
			update_embed = discord.Embed(
				colour=discord.Colour.green(),
				title="",
				description=f"An error occured while trying to change the volume.\n{Error}")
			await ctx.send(embed = update_embed)
			return


		#if not isinstance(source, discord.PCMVolumeTransformer):
		#        return await ctx.send("This source doesn't support adjusting volume or "
		#                              "the interface to do so is not exposed.")

		#number = int(number)/100
		#print(number)

		#voice.source.volume = int(number)