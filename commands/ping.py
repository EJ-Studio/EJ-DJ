from packages.CRITICAL.CLIENT import client
import discord
from commands.data import FOOTER, BOT_CHANNELS


@client.command(pass_context=True, aliases=["Ping"])
async def ping(ctx):
	if ctx.channel.name in BOT_CHANNELS.channels:
		pong1 = (round(client.latency * 1000))

		if pong1 >= 500:
			update_embed = discord.Embed(
				colour=discord.Colour.red(),
				title="",
				description=f"Pong!: {pong1}ms\nSpeeds are not looking good, Please ask a staff member or dev to restart the bot.")
			await ctx.send(embed = update_embed)

		elif pong1 >= 300:
			update_embed = discord.Embed(
				colour=discord.Colour.gold(),
				title="",
				description=f"Pong!: {pong1}ms\nSpeeds are looking slow...")
			await ctx.send(embed = update_embed)

		else:
			update_embed = discord.Embed(
				colour=discord.Colour.green(),
				title="",
				description=f"Pong!: {pong1}ms\nSpeeds are looking fast!")
			await ctx.send(embed = update_embed)