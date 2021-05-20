import discord
from discord.ext import commands
from discord.utils import get
from packages.CRITICAL.CLIENT import client
import platform
from packages.CRITICAL.VERSION import EJ_DJ_VERSION
from packages.CRITICAL.STATUS import EJ_DJ_STATUS
import os
import math
import subprocess
import sys
from importlib import reload
from commands.data import FOOTER, BOT_CHANNELS

#import ptdraft
#sys.path.append('../packages.CRITICAL.STATUS')

@client.command(pass_context=True, aliases=["Status"])
async def status(ctx, option):
	if ctx.channel.name in BOT_CHANNELS.channels:
		from packages.CRITICAL.STATUS import EJ_DJ_STATUS
		EJ_DJ_STATUS = EJ_DJ_STATUS

		if EJ_DJ_STATUS == option.upper():
			update_embed = discord.Embed(
			colour=discord.Colour.green(),
			title="",
			description=f"{option} is already in effect.")
			sent = await ctx.send(embed = update_embed)
			pass

		if option == "online" or option == "idle" or option == "offline":
			if option.upper() == "OFFLINE":

				client.remove_command('stop')

				client.remove_command('info')
				client.remove_command('Info')

				client.remove_command('update')
				client.remove_command('Update')

				client.remove_command('server')
				client.remove_command('Server')

				client.remove_command('join')

				client.remove_command('resume')

				client.remove_command('pause')

				client.remove_command('ping')

	#-----------THE play.py module commands-----------------
				client.remove_command('downlaod')
				client.remove_command('d')
				client.remove_command('Downlaod')

				client.remove_command('play')
				client.remove_command('p')
				client.remove_command('Play')

				client.remove_command('skip')
				client.remove_command('s')
				client.remove_command('Skip')

				client.remove_command('queue')
				client.remove_command('q')
				client.remove_command('Queue')

				client.remove_command('clear')
				client.remove_command('c')
				client.remove_command('Clear')

				client.remove_command('radio')
				client.remove_command('r')
				client.remove_command('Radio')

				client.remove_command('leave')

			elif option.upper() == "ONLINE":
				try:
					from commands import join, leave, play, ping, pause, resume, stop, update, server, download, info, change_status
				except:
					pass

			path = r'./packages/CRITICAL/'
			savesave = os.path.join(path, 'STATUS.py')
			f = open(savesave, "w")
			f.write("EJ_DJ_STATUS = '" + str(option.upper()) + "'")                         #player name save.
			f.close()

			update_embed = discord.Embed(
			colour=discord.Colour.green(),
			title="",
			description=f"Done!")
			sent = await ctx.send(embed = update_embed)
			return

		else:
			update_embed = discord.Embed(
			colour=discord.Colour.green(),
			title="",
			description=f"{option} is an invalid option.")
			sent = await ctx.send(embed = update_embed)
			return
# EJ_DJ_STATUS = "ONLINE"