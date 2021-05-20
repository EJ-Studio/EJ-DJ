import discord
from packages.CRITICAL.CLIENT import client
from commands.data import FOOTER, BOT_CHANNELS

@client.command(pass_context=True, aliases=["Leave"])
async def leave(ctx):
	if ctx.channel.name in BOT_CHANNELS.channels:
		
		if ctx.voice_client is None: #This should check if the bot is playing music.


			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="",
				description=f"Not currently in this channel.")
			await ctx.send(embed = update_embed)

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.green(),
				title="",
				description=f"Leaving channel.")
			await ctx.send(embed = update_embed)

			await ctx.voice_client.disconnect()
			return
