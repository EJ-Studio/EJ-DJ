import discord
from packages.CRITICAL.CLIENT import client
from commands.data import FOOTER, BOT_CHANNELS



@client.command(pass_context=True, aliases=["Join"])
async def join(ctx):
	if ctx.channel.name in BOT_CHANNELS.channels:
		try:
			if ctx.voice_client is None: #This should check if the bot is connected to a voice channel.

				channel = ctx.author.voice.channel
				await channel.connect()

				update_embed = discord.Embed(
					colour=discord.Colour.green(),
					title="",
					description=f"Joined channel!")
				await ctx.send(embed = update_embed)

			else:
				update_embed = discord.Embed(
					colour=discord.Colour.gold(),
					title="",
					description=f"Already joined this channel.")
				await ctx.send(embed = update_embed)

		except Exception as Error:
			#print(Error)
			#print("The bot is already connect to the channel.")
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="",
				description=f"You are not in a voice channel.")

			await ctx.send(embed = update_embed)