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


# @client.command(pass_context=True, aliases=["Info"])
# async def info(ctx):
#     if ctx.channel.name in BOT_CHANNELS.channels:
#         pfp = client.user.avatar_url

#         update_embed = discord.Embed(
#             colour=discord.Colour.green(),
#             title="Info",
#             description=f"EJ DJ V{EJ_DJ_VERSION}")

#         update_embed.set_author(name="EJ DJ", icon_url=(pfp))
#         update_embed.set_thumbnail(url=(pfp))

#         update_embed.add_field(name="Information:", value="""
#             EJ DJ is a music bot that is being developed by EJ Studios - Happypat900 for MatrixCraft.\n
#             Music bots are very buggy at times and may experience a lot of downtime unexpectedly for long periods, please be patient as these things are very common.\n
#             If you ever want to know the status of the bot, be sure to check in on the MatrixCraft server!\n
#             If you find a bug and wish to report it, please contact\n@EJ Studios#3379 or @Happypat900#8268\n

#             **Playlist:**
#             In order to create a playlist you must like a song. To do this You must play a song by either using:
#             >play or >radio. You cant like a song if their is no music playing.
#             Thank you for reading the info page!
#             """, inline=True)

#         update_embed.set_footer(text=f"{FOOTER.footer}")

#         await ctx.send(embed = update_embed)
'''
EJ DJ strives to bring the best, fastest and most highest quality audio whilsts being easy to use and bug free.
'''

@client.command(pass_context=True, aliases=["Info"])
async def info(ctx):

    pfp = client.user.avatar_url

    pages = 14
    cur_page = 1

    info_1 = discord.Embed(
        colour=discord.Colour.green(),
        title="Information",
        description=f"EJ DJ V{EJ_DJ_VERSION}.")
    info_1.set_author(name="EJ DJ", icon_url=(pfp))
    info_1.set_thumbnail(url=(pfp))
    info_1.add_field(name="About:", value="""
        EJ DJ is a music bot with community advantages, in development by EJ Studios - Happypat900 for MatrixAnarchy

        Music bots can be hard to maintain at times and may experience prolonged downtimes, Please be patient if the bot
        is in the offline state.

        If you would like know the bots status you can check its discord status or run the >server command in #bot-commands

        If you stumble upon a bug or have a question or suggestion, please PM @EJ Studios#3379 or @Happypat900#8268
        -@EJ Studios#3379  | Technical support, code base of EJ DJ.
        -@Happypat900#8268 | Server support , audio quality base of EJ DJ.

        Please continue to find more support by reacting... 
        """, inline=True)
    info_1.set_footer(text=f"Page 1/{pages} \n{FOOTER.footer}")

    #PLAY COMMAND----------------
    info_2 = discord.Embed(
        colour=discord.Colour.green(),
        title=">play",
        description=f"The main play command.")
    info_2.set_author(name="EJ DJ", icon_url=(pfp))
    info_2.set_thumbnail(url=(pfp))
    info_2.add_field(name=">play | >Play | >p",
        value="""
        Plays the song following the command, E.G:\n
        >play mmm by troyboi
        or
        >play https://music.youtube.com/watch?v=lbHRvGrNkhA&feature=share

        If you are in a voice chat you can do this command and the bot will
        automatically join your channel and start playing.
        """, inline=True)
    info_2.set_footer(text=f"Page 2/{pages} \n{FOOTER.footer}")

    #PAUSE COMMAND--------------------
    info_3 = discord.Embed(
        colour=discord.Colour.green(),
        title=">pause",
        description=f"The main pause command.")
    info_3.set_author(name="EJ DJ", icon_url=(pfp))
    info_3.set_thumbnail(url=(pfp))
    info_3.add_field(name=">pause | >Pause",
        value="""
        Pauses any current playing music.
        Works for:
        >play
        >radio
        >playlist.
        """, inline=True)
    info_3.set_footer(text=f"Page 3/{pages} \n{FOOTER.footer}")

    #RESUME COMMAND---------------------
    info_4 = discord.Embed(
        colour=discord.Colour.green(),
        title=">resume",
        description=f"The main resume command.")
    info_4.set_author(name="EJ DJ", icon_url=(pfp))
    info_4.set_thumbnail(url=(pfp))
    info_4.add_field(name=">resume | >Resume",
        value="""
        Resumes any paused music.\n
        Works for any paused music.
        """, inline=True)
    info_4.set_footer(text=f"Page 4/{pages} \n{FOOTER.footer}")

    info_5 = discord.Embed(
        colour=discord.Colour.green(),
        title=">join",
        description=f"The main join command.")
    info_5.set_author(name="EJ DJ", icon_url=(pfp))
    info_5.set_thumbnail(url=(pfp))
    info_5.add_field(name=">join | >Join",
        value="""
        Joins the bot to your current voice chat.\n
        If you are not in a voice chat the bot should notify you.
        """, inline=True)
    info_5.set_footer(text=f"Page 5/{pages} \n{FOOTER.footer}")

    info_6 = discord.Embed(
        colour=discord.Colour.green(),
        title=">leave",
        description=f"The main leave command.")
    info_6.set_author(name="EJ DJ", icon_url=(pfp))
    info_6.set_thumbnail(url=(pfp))
    info_6.add_field(name=">leave | >Leave",
        value="""
        Makes the bot leave your voice channel\n
        If you are not in a voice chat the bot should notify you.
        """, inline=True)
    info_6.set_footer(text=f"Page 6/{pages} \n{FOOTER.footer}")

    info_7 = discord.Embed(
        colour=discord.Colour.green(),
        title=">skip",
        description=f"The main skip command.")
    info_7.set_author(name="EJ DJ", icon_url=(pfp))
    info_7.set_thumbnail(url=(pfp))
    info_7.add_field(name=">skip | >Skip | >s | >stop | >Stop",
        value="""
        Makes the bot skip the current playing song\n
        If you are not in a voice chat the bot should notify you.
        """, inline=True)
    info_7.set_footer(text=f"Page 7/{pages} \n{FOOTER.footer}")

    info_8 = discord.Embed(
        colour=discord.Colour.green(),
        title=">update",
        description=f"The main update command.")
    info_8.set_author(name="EJ DJ", icon_url=(pfp))
    info_8.set_thumbnail(url=(pfp))
    info_8.add_field(name=">leave | >Leave",
        value="""
        Makes the bot leave your voice channel\n
        If you are not in a voice chat the bot should notify you.
        """, inline=True)
    info_8.set_footer(text=f"Page 8/{pages} \n{FOOTER.footer}")

    info_9 = discord.Embed(
        colour=discord.Colour.green(),
        title=">radio",
        description=f"The main radio command.")
    info_9.set_author(name="EJ DJ", icon_url=(pfp))
    info_9.set_thumbnail(url=(pfp))
    info_9.add_field(name=">radio | >Radio | >r",
        value="""
        Starts a random selection of all the downloaded song the bot has.

        To leave this, please just type " stop radio "
        
        If you are in a voice chat you can do this command and the bot will
        automatically join your channel and start playing.
        """, inline=True)
    info_9.set_footer(text=f"Page 9/{pages} \n{FOOTER.footer}")

    info_10 = discord.Embed(
        colour=discord.Colour.green(),
        title=">playlist",
        description=f"The main playlist command.")
    info_10.set_author(name="EJ DJ", icon_url=(pfp))
    info_10.set_thumbnail(url=(pfp))
    info_10.add_field(name=">leave | >Leave",
        value="""
        Starts your playlist in random order.

        To leave this, please just type " stop playlist "

        Your playlist is all of your liked songs you can read more about
        this using the >info command under >like.

        If you are in a voice chat you can do this command and the bot will
        automatically join your channel and start playing.
        """, inline=True)
    info_10.set_footer(text=f"Page 10/{pages} \n{FOOTER.footer}")

    info_11 = discord.Embed(
        colour=discord.Colour.green(),
        title=">server",
        description=f"The main server command.")
    info_11.set_author(name="EJ DJ", icon_url=(pfp))
    info_11.set_thumbnail(url=(pfp))
    info_11.add_field(name=">server | >Server",
        value="""
        >server shows you all of the server stats on the left side titled
        SERVER, and the bots statuses shown on the right titled BOT.

        SERVER:
            -The system is the current operating system the bot is on.
            -Storage is the total amount of song data stored.
            -Songs is how many songs the bot has downloaded.
            -Streaming is if the bot is doing a radio or playlist.
        BOT:
            -Status is the bots current status.
            -Ping is the rate in which the bot goes through discord and then to you.
            -Updates is if the bot has a critical update available.
        """, inline=True)
    info_11.set_footer(text=f"Page 11/{pages} \n{FOOTER.footer}")

    info_12 = discord.Embed(
        colour=discord.Colour.green(),
        title=">ping",
        description=f"The main ping command.")
    info_12.set_author(name="EJ DJ", icon_url=(pfp))
    info_12.set_thumbnail(url=(pfp))
    info_12.add_field(name=">ping | >Ping",
        value="""
        >ping quickly returns the amount of time taken for our server to reach discord
        and get to your ears.
        """, inline=True)
    info_12.set_footer(text=f"Page 12/{pages} \n{FOOTER.footer}")

    info_13 = discord.Embed(
        colour=discord.Colour.green(),
        title=">like",
        description=f"The main like command.")
    info_13.set_author(name="EJ DJ", icon_url=(pfp))
    info_13.set_thumbnail(url=(pfp))
    info_13.add_field(name=">like | >Like",
        value="""
        >like allows you to like a song and have it play using the >playlist
        command.

        If you dont already have a profile it will automatically create on.
        """, inline=True)
    info_13.set_footer(text=f"Page 13/{pages} \n{FOOTER.footer}")

    info_14 = discord.Embed(
        colour=discord.Colour.green(),
        title=">unlike",
        description=f"The main unlike command.")
    info_14.set_author(name="EJ DJ", icon_url=(pfp))
    info_14.set_thumbnail(url=(pfp))
    info_14.add_field(name=">unlike | >Unlike",
        value="""
        >unlike allows you to unlike a song that you have previously liked.

        If you dont have a profile you should recieve a warning telling you.

        To create a profile simply like a song.
        """, inline=True)
    info_14.set_footer(text=f"Page 14/{pages} \n{FOOTER.footer}")



    message = await ctx.send(embed = info_1)
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

                elif cur_page == 4:
                    await message.edit(embed=info_4)

                elif cur_page == 5:
                    await message.edit(embed=info_5)

                elif cur_page == 6:
                    await message.edit(embed=info_6)

                elif cur_page == 7:
                    await message.edit(embed=info_7)

                elif cur_page == 8:
                    await message.edit(embed=info_8)

                elif cur_page == 9:
                    await message.edit(embed=info_9)

                elif cur_page == 10:
                    await message.edit(embed=info_10)

                elif cur_page == 11:
                    await message.edit(embed=info_11)

                elif cur_page == 12:
                    await message.edit(embed=info_12)

                elif cur_page == 13:
                    await message.edit(embed=info_13)

                elif cur_page == 14:
                    await message.edit(embed=info_14)
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

                elif cur_page == 4:
                    await message.edit(embed=info_4)

                elif cur_page == 5:
                    await message.edit(embed=info_5)

                elif cur_page == 6:
                    await message.edit(embed=info_6)

                elif cur_page == 7:
                    await message.edit(embed=info_7)

                elif cur_page == 8:
                    await message.edit(embed=info_8)

                elif cur_page == 9:
                    await message.edit(embed=info_9)

                elif cur_page == 10:
                    await message.edit(embed=info_10)

                elif cur_page == 11:
                    await message.edit(embed=info_11)

                elif cur_page == 12:
                    await message.edit(embed=info_12)

                elif cur_page == 13:
                    await message.edit(embed=info_13)

                elif cur_page == 14:
                    await message.edit(embed=info_14)
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