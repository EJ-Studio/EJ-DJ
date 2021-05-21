import discord
import youtube_dl
import os
#import ffprobe
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from packages.CRITICAL.CLIENT import client
from packages.CRITICAL.VERSION import EJ_DJ_VERSION
import asyncio
import subprocess
import urllib.request
import re #regulare expression
from shutil import copyfile
from commands.data import FOOTER, BOT_CHANNELS




# @client.event
# async def on_raw_reaction_add(payload):
#     print("SOMEONE REACTED")



# @client.command(pass_context=True, aliases=["Update"])
# async def update(ctx):
#     if ctx.channel.name in BOT_CHANNELS.channels:

#         pfp = client.user.avatar_url

#         update_embed = discord.Embed(
#             colour=discord.Colour.green(),
#             title="UPDATE",
#             description=f"EJ DJ V{EJ_DJ_VERSION}")

#         update_embed.set_author(name="Trinity", icon_url=(pfp))
#         update_embed.set_thumbnail(url=(pfp))

#         update_embed.add_field(name="NEW:", value="""
#             -PROFILES!!!\n
#             -Changed the radio stop command to " stop radio ".\n
#             -Updated the help channel.
#             """, inline=True)

#         update_embed.add_field(name="FIXED:", value="""
#             -Fixed the stop command from sometimes causing file leaks.
#             """, inline=True)

#         update_embed.add_field(name="KNOWN BUGS:", value="""
#             -Their is a known bug when trying to play 2 songs at the same time.
#             """, inline=True)

#         update_embed.add_field(name="Report:", value="""
#             If you find a bug and wish to report it, please contact\n@EJ Studios#3379 or @Happypat900#8268
#             """, inline=False)

#         update_embed.set_footer(text=f"{FOOTER.footer}")

#         await ctx.send(embed = update_embed)





































@client.command(pass_context=True, aliases=["Update"])
async def update(ctx):

    pfp = client.user.avatar_url

    pages = 3
    cur_page = 2 #Change this to the current update !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    info_1 = discord.Embed(
        colour=discord.Colour.green(),
        title="UPDATE",
        description=f"EJ DJ V0.0.0")
    info_1.set_author(name="EJ DJ", icon_url=(pfp))
    info_1.set_thumbnail(url=(pfp))
    info_1.add_field(name="NEW:", value="""
        -PROFILES!!!\n
        -Changed the radio stop command to " stop radio ".\n
        -Updated the help channel.
        """, inline=True)

    info_1.add_field(name="FIXED:", value="""
        -Fixed the stop command from sometimes causing file leaks.
        """, inline=True)

    info_1.add_field(name="KNOWN BUGS:", value="""
        -Their is a known bug when trying to play 2 songs at the same time.
        """, inline=True)

    info_1.add_field(name="Report:", value="""
        If you find a bug and wish to report it, please contact\n@EJ Studios#3379
        """, inline=False)

    info_1.set_footer(text=f"Page 1/{pages} \n{FOOTER.footer}")



    info_2 = discord.Embed(
        colour=discord.Colour.green(),
        title="UPDATE",
        description=f"EJ DJ V0.0.1")
    info_2.set_author(name="EJ DJ", icon_url=(pfp))
    info_2.set_thumbnail(url=(pfp))
    info_2.add_field(name="NEW:", value="""
        -Redone the whole update command to make it more modern while still keeping it user friendly.\n
        -Added a server restart for times when the bot gets completely emotional... (ADMIN ONLY)\n
        """, inline=True)

    info_2.add_field(name="FIXED:", value="""
        -Fixed a bug that caused the automatic status changes to pause if the internet went out or was weak.
        """, inline=True)

    info_2.add_field(name="KNOWN BUGS:", value="""
        -No known bugs at this time!
        """, inline=True)

    info_2.add_field(name="Report:", value="""
        If you find a bug and wish to report it, please contact\n@EJ Studios#3379
        """, inline=False)

    info_2.set_footer(text=f"Page 2/{pages} \n{FOOTER.footer}")


    info_3 = discord.Embed(
        colour=discord.Colour.green(),
        title="UPDATE",
        description=f"EJ DJ V0.0.2 BETA")
    info_3.set_author(name="EJ DJ", icon_url=(pfp))
    info_3.set_thumbnail(url=(pfp))
    info_3.add_field(name="Whats next?", value="""
        -We are still looking at what to improve for our next update, check back soon!
        """, inline=True)

    info_3.add_field(name="Have an idea?", value="""
        please contact: @EJ Studios#3379
        """, inline=False)

    info_3.set_footer(text=f"Page 3/{pages} \n{FOOTER.footer}")


















    message = await ctx.send(embed = info_2) #Change this to the current update !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    #adds reactions.

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                if cur_page == 1:
                    await message.edit(embed=info_1)

                elif cur_page == 2:
                    await message.edit(embed=info_2)

                elif cur_page == 3:
                    await message.edit(embed=info_3)

                # await message.edit(embed=info)
                await message.remove_reaction(reaction, user)


            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1

                if cur_page == 1:
                    await message.edit(embed=info_1)

                elif cur_page == 2:
                    await message.edit(embed=info_2)

                elif cur_page == 3:
                    await message.edit(embed=info_3)
                #await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds