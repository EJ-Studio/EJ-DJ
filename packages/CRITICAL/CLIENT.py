import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True

try:
	client = commands.Bot(command_prefix=">", help_command=None, intents=intents)
except:
	print("gotcha")
