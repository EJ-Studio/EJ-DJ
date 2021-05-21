import discord
from discord.ext import commands
from discord.utils import get
import packages
import packages.CRITICAL
from packages.CRITICAL.CLIENT import client
from sys import platform

from packages.CRITICAL.VERSION import EJ_DJ_VERSION
from packages.CRITICAL.STATUS import EJ_DJ_STATUS
import os
import math
import subprocess
import sys
from importlib import reload
from commands.data import FOOTER, BOT_CHANNELS

@client.command(pass_context=True, aliases=["Server"])
async def server(ctx):
	if ctx.channel.name in BOT_CHANNELS.channels:

		update_embed = discord.Embed(
			colour=discord.Colour.green(),
			title="",
			description=f"Loading please wait <a:loading:768429190193086475>")
		sent = await ctx.send(embed = update_embed)

		if platform == "linux" or platform == "linux2":
			system2 = "Linux"
		elif platform == "darwin":
			system2 = "Linux"
		elif platform == "win32":
			system2 = "Windows"

		#system2 = platform.uname()

		pfp = client.user.avatar_url

		update_embed = discord.Embed(
			colour=discord.Colour.green(),
			title="SERVER",
			description=f"EJ DJ V{EJ_DJ_VERSION}")

		update_embed.set_author(name="EJ DJ", icon_url=(pfp))
		update_embed.set_thumbnail(url=(pfp))

		fp = r"./cached_songs/"
		file = int(0)

		file = os.listdir(fp)
		files = len(file)


		path = r"./cached_songs/"
		total = 0
		for entry in os.scandir(path):
			if entry.is_file():
				total += entry.stat().st_size
			elif entry.is_dir():
				total += folder_size(entry.path)

		if total == 0:
			print("0B")

		else:
			size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
			i = int(math.floor(math.log(total, 1024)))
			p = math.pow(1024, i)
			s = round(total / p, 2)
			total = ("%s %s" % (s, size_name[i]))

		
		voice = get(client.voice_clients, guild=ctx.guild)
		try:
			if voice.is_playing():
				is_playing = True
				pass
			elif voice.is_paused():
				is_playing = "Paused"
				pass
			else:
				is_playing = False
				pass
		except:
			is_playing = False
			pass

			
		update_embed.add_field(name="SERVER:", value=f"""
			-System: {system2}\n
			-Storage: {total}\n
			-Songs: {files}\n
			-Streaming: {is_playing}
			""", inline=True)

		#update_embed.add_field(name="SERVER:", value=f"""
			#-System: {system2.system}\n
			#-Memory: {psutil.virtual_memory()}\n
			#-Number of processors: {system1.NumberOfProcessors}\n
			#-System type: {system1.SystemType}\n
			#-Processor: {system2.processor}
			#""", inline=True)





		reload(packages.CRITICAL.STATUS)
		EJ_DJ_STATUS = packages.CRITICAL.STATUS.EJ_DJ_STATUS

		if EJ_DJ_STATUS == "ONLINE":
			ono = client.get_emoji(782527423669469184)
			msg1 = "Online"
			#status = ("Online   <a:online:782527423669469184>")
							#<a:loading:768429190193086475>
		elif EJ_DJ_STATUS == "IDLE":
			ono = client.get_emoji(782540894988795904)
			msg1 = "Under maintenance"
			print(EJ_DJ_STATUS)

		else:
			ono = client.get_emoji(782527932907651113)
			msg1 = "Critical error"

		pong = (round(client.latency * 1000))

		if pong >= 500:
			ping = pong
			msg2 = "Sorry we are experiencing delays"

		elif pong >= 300:
			ping = pong
			msg2 = "Speeds are slow"

		else:
			ping = pong
			msg2 = "Speeds are fast"
		pass

		if platform == "linux" or platform == "linux2":
			command = ['pip3', 'list', '--outdated']
			result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()
			if "youtube_dl" in result or "youtube-dl" in result:
				msg3 = "youtube-dl is out of date, some fetures may not work" #RUN THIS: pip install youtube_dl --upgrade
				pass
			else:
				msg3 = "Up to date"
				pass

		elif platform == "darwin":
			command = ['pip3', 'list', '--outdated']
			result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()
			if "youtube_dl" in result or "youtube-dl" in result:
				msg3 = "youtube-dl is out of date, some fetures may not work" #RUN THIS: pip install youtube_dl --upgrade
				pass
			else:
				msg3 = "Up to date"
				pass

		elif platform == "win32":
			command = ['pip', 'list', '--outdated']
			result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()
			if "youtube_dl" in result or "youtube-dl" in result:
				msg3 = "youtube-dl is out of date, some fetures may not work" #RUN THIS: pip install youtube_dl --upgrade
				pass
			else:
				msg3 = "Up to date"
				pass
		# else:
		# 	msg3 = "Error"
		# command = ['pip', 'list', '--outdated']
		# result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()

		# if "youtube_dl" in result or "youtube-dl" in result:
		# 	msg3 = "youtube-dl is out of date, some fetures may not work" #RUN THIS: pip install youtube_dl --upgrade
		# else:
		# 	msg3 = "Up to date"

		update_embed.add_field(name="BOT:", value=f"""
			-Status: {ono} | {msg1}\n
			-Ping: {ping} | {msg2}\n
			-Updates: {msg3} 
			""", inline=True)
		update_embed.set_footer(text=f"{FOOTER.footer}")

		await sent.delete()
		await ctx.send(embed = update_embed)
# import subprocess
# import sys



# command=['pip', 'list', '--outdated']
# result=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()
# print(result)
# print("_____________________________________________________")
# if "youtube_dl" in result or "youtube-dl" in result:
#     print("True")

# import wmi
 
# c = wmi.WMI()    
# my_system = c.Win32_ComputerSystem()[0]
 
# print(f"Manufacturer: {my_system.Manufacturer}")
# print(f"Model: {my_system. Model}")
# print(f"Name: {my_system.Name}")
# print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
# print(f"SystemType: {my_system.SystemType}")
# print(f"SystemFamily: {my_system.SystemFamily}")