import discord
import youtube_dl
import os
#import ffprobe
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from packages.CRITICAL.CLIENT import client
import asyncio
import subprocess
import urllib.request
import re #regulare expression
from shutil import copyfile
from commands.data import FOOTER, BOT_CHANNELS

client.remove_command('download')

@client.command(pass_context=True, aliases=['d', 'Download'])
async def download(ctx, *, url1 ):
	if ctx.channel.name in BOT_CHANNELS.channels:
		if url1 == "":
			update_embed = discord.Embed(
				colour=discord.Colour.green(),
				title="",
				description=f"Please make sure to specify the song and author, or give a valid youtube link.")
			await ctx.send(embed = update_embed)

		url1 = url1.replace(" ", "-") #hello-their, my-friend
		url1 = url1.replace(",", " ") #hello-their my-friend
		#url = [url]
		url1 = list((url1.split(" ")) ) #['hello-their', '-my-friend'
		url1 = [x.replace("-", " ") for x in url1]
		try:
			url1 = [x.replace(" ", "") for x in url1]
		except:
			pass
		#url = url.replace("-", "")
		print(url1)

		try:
			for number in range(len(url1)):
				print(url1[number])
				url = url1[number]

				if "https://" not in url:
					#await ctx.message.delete()

					url = url.replace(" ", "+")
					#print(url)
					html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url}")
					#print(html.read().decode())
					video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
					#print(video_ids[0])
					url = f"https://www.youtube.com/watch?v={video_ids[0]}"
				else:
					pass
				ydl_opts = {
					'format': 'bestaudio/best',
					'postprocessors': [{
						'key': 'FFmpegExtractAudio',
						'preferredcodec': 'mp3',
						'preferredquality': '192',
					}],
				}
				with youtube_dl.YoutubeDL(ydl_opts) as ydl:
					try:
						ydl_opts = {}#{"outtmpl": path}
						with youtube_dl.YoutubeDL(ydl_opts) as yd:
							meta = yd.extract_info(url, download=False) 
							song_name = (meta['title'])
							song_duration = (meta['duration'])

						if song_duration <= 599:
							update_embed = discord.Embed(
								colour=discord.Colour.green(),
								title="",
								description=f"Preparing songs for downlaod")

							preparing_embed = await ctx.send(embed = update_embed)

							if os.path.isfile(rf'./cached_songs/{song_name}.mp3'):

								await preparing_embed.delete()

								update_embed = discord.Embed(
									colour=discord.Colour.green(),
									title="",
									description=f"The song: {song_name} already exists.")
								await ctx.send(embed = update_embed)
								continue

							else:
								update_embed = discord.Embed(
									colour=discord.Colour.green(),
									title="",
									description=f"Downloading {song_name} <a:loading:800325670613286952>")
								sent = await ctx.send(embed = update_embed)

								try:
									ydl.download([url])
									await sent.delete()
									await preparing_embed.delete()

								except Exception as Error:
									await sent.delete()
									await preparing_embed.delete()
									update_embed = discord.Embed(
										colour=discord.Colour.red(),
										title="",
										description=f"Error downloading song...")
									await ctx.send(embed = update_embed)
									continue

								#IF THE SONGS IS SUCCESSFULLY DOWNLOADED:
								update_embed = discord.Embed(
										colour=discord.Colour.green(),
										title="",
										description=f"Downloaded {song_name} successfully.")
								await ctx.send(embed = update_embed)

								
								for file in os.listdir("./"):
									if file.endswith(".mp3"):
										if '"' in song_name:
											print("YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
											song_name = file[:-12]
											print(song_name)
										try:
											os.rename(file, f'{song_name}.mp3')
											if os.path.isfile(f'./cached_songs/{song_name}.mp3'):
												continue

											else:
												try:
													copyfile(f"./{song_name}.mp3", f"./cached_songs/{song_name}.mp3")
													os.remove(rf"./{song_name}.mp3")
													continue
												except Exception as Error:
													print("died here because: ", Error)
										except:
											pass

						elif song_duration >= 600:
							update_embed = discord.Embed(
								colour=discord.Colour.green(),
								title="",
								description=f"Can not downlaod {song_name} because it is : {(round((song_duration)/60))} minutes long.")

							await ctx.send(embed = update_embed)
							pass
					except:
						pass

		except Exception as Error:
			print("An error hapend at the for loop because:\n", Error)