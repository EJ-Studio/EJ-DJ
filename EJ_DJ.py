#Matrixcraft music bot.py developed for Matrixcraft by EJ Studios and Patrick.

import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound

from packages.CRITICAL.TOKEN import TOKEN
from packages.CRITICAL.CLIENT import client
from packages.CRITICAL.STATUS import EJ_DJ_STATUS
from commands.data import FOOTER, BOT_CHANNELS

import asyncio, youtube_dl

import random
import time
from importlib import reload
import os
import subprocess, sys
from sys import platform

from shutil import copyfile

import packages
import packages.CRITICAL
from packages.CRITICAL.STATUS import EJ_DJ_STATUS
from packages.CRITICAL.TOKEN import TOKEN
from packages.CRITICAL.CLIENT import client
from packages.CRITICAL.VERSION import EJ_DJ_VERSION

import commands #Reloading the modules (>REFRESH) will not work without this imported...
from commands import join, play, ping, pause, resume, update, server, download, info, change_status#, join_event, leave_event

# #TEST
# from PIL import Image, ImageDraw, ImageFont
# import urllib.request
# import io
# from discord import File

global has_connected
has_connected = False

global Create_Task_Error
Create_Task_Error = 0

@client.event
async def on_ready():
    global has_connected
    if has_connected:
        await on_reconnect()
    else:
        has_connected = True
        print('We have logged in as {0.user}'.format(client))
        print("Name: {}".format(client.user.name))
        print("ID: {}".format(client.user.id))

        global task_1, task_2
        task_1 = client.loop.create_task(change_status())
        task_2 = client.loop.create_task(check_update())

async def on_reconnect():
    print('We have faced technical difficulty\'s')
    client.loop.create_task(change_status())
    client.loop.create_task(check_update())

async def change_status():
    await client.wait_until_ready()#waits until bot is ready.

    while True:
        try:
            reload(packages.CRITICAL.STATUS)
            EJ_DJ_STATUS = packages.CRITICAL.STATUS.EJ_DJ_STATUS
            #print(EJ_DJ_STATUS)

            if EJ_DJ_STATUS == "ONLINE":
                activity = discord.Game(name=f"EJ DJ V{EJ_DJ_VERSION} | {FOOTER.footer}")
                await client.change_presence(status=discord.Status.online, activity=activity)
                await asyncio.sleep(10)

                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=">Help"))
                #activity = discord.Game(name="try: >Help")
                #await client.change_presence(status=discord.Status.online, activity=activity)
                await asyncio.sleep(10)
                #reload(EJ_DJ_STATUS)
                continue
            elif EJ_DJ_STATUS == "IDLE":
                activity = discord.Game(name=f"EJ DJ V{EJ_DJ_VERSION} | Under maintenance")
                await client.change_presence(status=discord.Status.idle, activity=activity)
                await asyncio.sleep(10)

                activity = discord.Game(name=f"Performing general upkeep | ETA: Unknown")
                await client.change_presence(status=discord.Status.idle, activity=activity)
                await asyncio.sleep(10)
                #reload(EJ_DJ_STATUS)
                continue
            elif EJ_DJ_STATUS == "OFFLINE":
                activity = discord.Game(name=f"OFFLINE | Collecting error information")
                await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
                await asyncio.sleep(10)

                activity = discord.Game(name=f"OFFLINE | A EJ Studios dev will be on it shortly")
                await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
                await asyncio.sleep(10)
                continue
            else:
                activity = discord.Game(name=f"EJ DJ V{EJ_DJ_VERSION} | {FOOTER.footer}")
                await client.change_presence(status=discord.Status.online, activity=activity)
                await asyncio.sleep(10)
                #reload(EJ_DJ_STATUS)
                continue
        except Exception as Error:
            global Create_Task_Error

            if Create_Task_Error == 0:
                print("\n\nSYSTEM : ERROR | An create_task command failed during operation.\n")

                print("SYSTEM : AUTO-FIX | Started.\n")

                print("AUTO-FIX | Checking for available updates.")
                print("__________________________________________")
                command = ['pip3', 'list', '--outdated']
                result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()

                if "youtube_dl" in result or "youtube-dl" in result:
                    print("youtube_dl is out of date, preparing to update it.")
                    while True:
                        command = ['pip3', 'install', 'youtube_dl', '--upgrade']
                        result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()

                        if "Successfully" in result:
                            print("updated youtube_dl successfully")
                            pass
                        else:
                            print("Retrying update.")
                            continue
                #msg3 = "youtube-dl is out of date, some fetures may not work" #RUN THIS: pip install youtube_dl --upgrade
                else:
                    print("Could not check update or updates are already up to date")
                    pass

                print("__________________________________________\n")

                print("\nAUTO-FIX | Checked updates successfully!\n")

                print("AUTO-FIX | Restarting 'change_status' and shutting down.")
                Create_Task_Error = 1
                client.loop.create_task(change_status())
                return

            elif Create_Task_Error >= 1:
                print("SYSTEM : ERROR | AUTO-FIX failed to fix issue.")
                print("SYSTEM : ERROR : REPORT | ", Error,"\n")

                print("SYSTEM : INFO | The system will now restart.\n")
                os.system("shutdown /r /t 0")
                return

async def check_update():
    await client.wait_until_ready()#waits until bot is ready.

    command = ['pip3', 'list', '--outdated']
    result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()

    if "youtube_dl" in result or "youtube-dl" in result:
        print("youtube_dl is out of date, preparing to update it.")

        while True:
            command = ['pip3', 'install', 'youtube_dl', '--upgrade']
            result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()

            if "Successfully" in result:
                print("updated youtube_dl successfully")
                return
            else:
                print("Retrying update.")
        #msg3 = "youtube-dl is out of date, some fetures may not work" #RUN THIS: pip install youtube_dl --upgrade
    else:
        print("youtube_dl is up to date!")






@client.command(pass_context=True, aliases=["help"])
async def Help(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:
        pfp = client.user.avatar_url

        Help_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="Bot commands",
            description=f"EJ DJ V{EJ_DJ_VERSION}")

        Help_embed.set_author(name="EJ DJ", icon_url=(pfp))
        Help_embed.set_thumbnail(url=(pfp))

        Help_embed.add_field(name=">Ping", value="Returns with the response time of the bot.", inline=True)
        Help_embed.add_field(name=">Play url", value="Playes the url you want on a voice channel.", inline=True)

        Help_embed.add_field(name="\u200b", value="\u200b")

        Help_embed.add_field(name=">pause", value="Pauses current playing music.", inline=True)
        Help_embed.add_field(name=">resume", value="Resumes the music.", inline=True)

        Help_embed.add_field(name="\u200b", value="\u200b")

        Help_embed.add_field(name=">join", value="Makes the bot join your current voice channel.", inline=True)
        Help_embed.add_field(name=">leave", value="Makes the bot leave your current voice channel.", inline=True)

        Help_embed.add_field(name="\u200b", value="\u200b")

        #Help_embed.add_field(name="\u200b", value="\u200b")

        Help_embed.add_field(name=">stop", value="Makes the music stop.", inline=True)
        Help_embed.add_field(name=">skip", value="Skipes to the next song in your queue.", inline=True)

        Help_embed.add_field(name="\u200b", value="\u200b")

        Help_embed.add_field(name=">update", value="See the lattest added fetures on EJ DJ!", inline=True)
        Help_embed.add_field(name=">info", value="See general information about the bot.", inline=True)

        Help_embed.add_field(name="\u200b", value="\u200b")

        Help_embed.add_field(name=">radio", value="Puts all of the bots downloaded songs on a random playlist!", inline=True)
        Help_embed.add_field(name="stop radio", value="Stops the radio from playing.", inline=True)

        Help_embed.add_field(name="\u200b", value="\u200b")

        Help_embed.add_field(name=">playlist", value="Plays your liked songs!", inline=True)
        Help_embed.add_field(name="stop playlist", value="Stops your playlist from playing.", inline=True)

        Help_embed.add_field(name="\u200b", value="\u200b")

        Help_embed.add_field(name=">server", value="See everything the bot is up too and stats.", inline=True)

        Help_embed.add_field(name="\u200b", value="\u200b")

        Help_embed.set_footer(text=f"{FOOTER.footer}")

        await ctx.send(embed = Help_embed)





@client.command()
# @commands.has_role("bot controller")
#@commands.is_owner()
async def SHUTDOWN(ctx):
    if str(ctx.message.author) != "EJ Studios#3379":
        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="System alert",
            description=f"You do not have permissions to perform this action.")
        await ctx.send(embed = update_embed)
        return

    if ctx.channel.name in BOT_CHANNELS.channels:
        role = discord.utils.get(ctx.guild.roles, name="bot controller")
        if role in ctx.author.roles:
            pass
        else:
            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="System alert",
                description=f"You do not have permission to perform this action.")
            await ctx.send(embed = update_embed)
            return


        activity = discord.Game(name="Shutting down")
        await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)

        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="System",
            description=f"Shutting down.")
        await ctx.send(embed = update_embed)
        await client.logout()

@client.command()
#@commands.is_owner()
async def REFRESH(ctx):

    if str(ctx.message.author) != "EJ Studios#3379":
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="System alert",
            description=f"You do not have permissions to perform this action.")
        await ctx.send(embed = update_embed)
        return

    if ctx.channel.name in BOT_CHANNELS.channels:
        role = discord.utils.get(ctx.guild.roles, name="bot controller")
        if role in ctx.author.roles:
            pass
        else:
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="System alert",
                description=f"You do not have permission to perform this action.")
            await ctx.send(embed = update_embed)
            return

    if ctx.channel.name in BOT_CHANNELS.channels:
        try:
            #patcomment await ctx.message.delete()
            activity = discord.Game(name="Refreshing...")
            await client.change_presence(status=discord.Status.idle, activity=activity)

            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="System",
                description=f"Refreshing...")
            restart_text1 = await ctx.send(embed = update_embed)
            #await ctx.send("Refreshing.")

            client.remove_command('info')
            client.remove_command('Info')
            reload(commands.info)

            client.remove_command('update')
            client.remove_command('Update')
            reload(commands.update)

            client.remove_command('server')
            client.remove_command('Server')
            reload(commands.server)

            client.remove_command('join')
            client.remove_command('Join')
            reload(commands.join)

            # client.remove_command('leave')
            # reload(commands.leave)

            client.remove_command('pause')
            client.remove_command('Pause')
            reload(commands.pause)

            client.remove_command('ping')
            client.remove_command('Ping')
            reload(commands.ping)

            client.remove_command('downlaod')
            client.remove_command('d')
            client.remove_command('Downlaod')
            reload(commands.download)

            client.remove_command('play')
            client.remove_command('p')
            client.remove_command('Play')

            client.remove_command('radio')
            client.remove_command('r')
            client.remove_command('Radio')

            client.remove_command('skip')
            client.remove_command('s')
            client.remove_command('Skip')

            client.remove_command('queue')
            client.remove_command('q')
            client.remove_command('Queue')

            client.remove_command('leave')

            client.remove_command('like')
            client.remove_command('Like')
            client.remove_command('unlike')
            client.remove_command('Unlike')
            client.remove_command('list')
            client.remove_command('List')

            client.remove_command('playlist')

            client.remove_command('delete_song')

            client.remove_command('clear')
            client.remove_command('c')
            client.remove_command('Clear')
            reload(commands.play)

            client.remove_command('resume')
            client.remove_command('Resume')
            reload(commands.resume)

            client.remove_command('status')
            reload(commands.change_status)

            activity = discord.Game(name="Done!")
            await client.change_presence(status=discord.Status.online, activity=activity)
            
            await restart_text1.delete()
            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="",
                description=f"Finished!")
            restart_text2 = await ctx.send(embed = update_embed)
            await asyncio.sleep(5)
            await restart_text2.delete()
            #await ctx.send("Done!")

        except Exception as Error:
            print("""
    An unexpected error has occured while restarting.
    """)
            print(Error)
            update_embed = discord.Embed(
                colour=discord.Colour.red(),
                title="System Error",
                description=f"Sorry an error has occurred.\nAn Matrixcraft dev will be on it soon!")
            await ctx.send(embed = update_embed)
            client.remove_command('stop')
            client.remove_command('info')
            client.remove_command('Info')
            client.remove_command('update')
            client.remove_command('Update')
            client.remove_command('server')
            client.remove_command('Server')
            client.remove_command('join')
            client.remove_command('Join')
            client.remove_command('resume')
            client.remove_command('Resume')
            client.remove_command('pause')
            client.remove_command('Pause')
            client.remove_command('ping')
            client.remove_command('Ping')
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
            client.remove_command('like')
            client.remove_command('Like')
            client.remove_command('unlike')
            client.remove_command('Unlike')
            client.remove_command('list')
            client.remove_command('List')
            client.remove_command('playlist')

            path = r'./packages/CRITICAL/'
            savesave = os.path.join(path, 'STATUS.py')
            f = open(savesave, "w")
            f.write("EJ_DJ_STATUS = '" + str("OFFLINE") + "'")                         #player name save.
            f.close()


@client.command(pass_context = True)
async def SERVER_RESTART(ctx):
    if str(ctx.message.author) != "EJ Studios#3379":
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="System alert",
            description=f"You do not have permissions to perform this action.")
        await ctx.send(embed = update_embed)
        return
    update_embed = discord.Embed(
        colour=discord.Colour.green(),
        title="System",
        description=f"Preparing the bot for the server restart <a:loading:768429190193086475>")
    info = await ctx.send(embed = update_embed)

    await client.wait_until_ready()
    activity = discord.Game(name=f"RESTARTING SERVER | Turning off the bot.")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    await asyncio.sleep(5)
    await client.wait_until_ready()

    await info.delete()

    update_embed = discord.Embed(
        colour=discord.Colour.green(),
        title="System",
        description=f"Restarting <a:animatedservericon:807182434068070401>")
    info = await ctx.send(embed = update_embed)

    await client.logout()

    os.system("shutdown /r /t 0")
    return

@client.command()
#@commands.is_owner()
async def RESTART(ctx):
    if str(ctx.message.author) != "EJ Studios#3379":
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="System alert",
            description=f"You do not have permissions to perform this action.")
        await ctx.send(embed = update_embed)
        return

    if ctx.channel.name in BOT_CHANNELS.channels:
        role = discord.utils.get(ctx.guild.roles, name="bot controller")
        if role in ctx.author.roles:
            pass
        else:
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="System alert",
                description=f"You do not have permission to perform this action.")
            await ctx.send(embed = update_embed)
            return

    if ctx.channel.name in BOT_CHANNELS.channels:
        role = discord.utils.get(ctx.guild.roles, name="bot controller")
        if role in ctx.author.roles:
            pass
        else:
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="System alert",
                description=f"You do not have permission to perform this action.")
            await ctx.send(embed = update_embed)
            return
        try:
            activity = discord.Game(name="Restarting...")
            await client.change_presence(status=discord.Status.idle, activity=activity)
            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="",
                description=f"Restarting...")
            await ctx.send(embed = update_embed)
            print("\nRESTARTING")

            await client.logout()

            if platform == "linux" or platform == "linux2":
                path = (r"python3 EJ_DJ.py")
            elif platform == "darwin":
                path = (r"python3 EJ_DJ.py")
            elif platform == "win32":
                path = (r"python EJ_DJ.py")

            os.system(path)
            #os.system("pause")

            # subprocess.Popen([r"python 'D:\\EJ Studios support bot\\EJ Studios bot.py'"],
            #     creationflags=subprocess.CREATE_NEW_CONSOLE)
            #exit()

            # p = subprocess.Popen(["powershell.exe", 
            #     "python 'EJ Studios bot.py'"], 
            #     stdout=sys.stdout)
            # p.communicate()
            #os.system('python "EJ Studios bot.py"')
            ##await asyncio.sleep(10)
            ##await ctx.send("Restart successful.")

        except Exception as Error:
            print(Error)
            update_embed = discord.Embed(
                colour=discord.Colour.red(),
                title="",
                description=f"Sorry an error has occurred.\nAn Matrixcraft dev will be on it soon!")
            await ctx.send(embed = update_embed)
            client.remove_command('stop')
            client.remove_command('info')
            client.remove_command('Info')
            client.remove_command('update')
            client.remove_command('Update')
            client.remove_command('server')
            client.remove_command('Server')
            client.remove_command('join')
            client.remove_command('Join')
            client.remove_command('resume')
            client.remove_command('Resume')
            client.remove_command('pause')
            client.remove_command('Pause')
            client.remove_command('ping')
            client.remove_command('Ping')
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
            client.remove_command('like')
            client.remove_command('Like')
            client.remove_command('unlike')
            client.remove_command('Unlike')
            client.remove_command('list')
            client.remove_command('List')
            client.remove_command('playlist')

            path = r'./packages/CRITICAL/'
            savesave = os.path.join(path, 'STATUS.py')
            f = open(savesave, "w")
            f.write("EJ_DJ_STATUS = '" + str("OFFLINE") + "'")                         #player name save.
            f.close()

@client.event
async def on_command_error(ctx, error):
    Error = str(error)
    print("\n\nCATCHED AN ERROR:" + Error + "\n")

    if "PermissionError:" in Error:
        print("PERMISSION ERROR<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        pass

    elif "FileNotFoundError:" in Error:
        print("FILE NOT FOUND ERROR<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        pass

    elif "IndexError:" in Error:
        print("Index Error<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        pass

    elif "Already playing audio." in Error:
        print("Failed to play audio because audio is currently playing.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        pass

    elif "url1 is a required argument that is missing." in Error:
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="",
            description=f">download - ERROR:\nPlease make sure to specify the song and author, or give a valid youtube link.")
        await ctx.send(embed = update_embed)

    elif "url is a required argument that is missing." in Error:
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="",
            description=f">play - ERROR:\nPlease make sure to specify the song and author, or give a valid youtube link.")
        await ctx.send(embed = update_embed)

    elif "Command" and "is not found" in Error:
        update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="",
            description=f">? - ERROR:\nPlease make sure that this command exists and you have permission to use it.")
        await ctx.send(embed = update_embed)

    else:
        reload(packages.CRITICAL.STATUS)
        EJ_DJ_STATUS = packages.CRITICAL.STATUS.EJ_DJ_STATUS
        
        if EJ_DJ_STATUS == "OFFLINE":
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description=f"Please wait until EJ DJ is back online.")
            await ctx.send(embed = update_embed)

        elif EJ_DJ_STATUS == "IDLE":
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description=f"Please wait for maintenance to finish and try again.")
            await ctx.send(embed = update_embed)



        else:
            update_embed = discord.Embed(
                colour=discord.Colour.red(),
                title="",
                description=f"Sorry, something bad happend.")
            await ctx.send(embed = update_embed)
            pass

# @play.error
#     async def play_handler(self, ctx, error):
#         if isinstance(error, commands.AttributeError):
#             await ctx.send("Please retry that.")
#         else:
#             await ctx.send("Please retry that.")



try:
    client.run(TOKEN)
except Exception as Error:
    print(f"System Error | Could not start the bot due to an unknown reason. Error: {Error}\n\nThe system will reboot in 1 minute")
    Time = 60
    while True:
        Time -= 1
        os.system('cls' if os.name == 'nt' else "printf '\033c'") #Clears the terminal.
        print(f"System Error | Could not start the bot due to an unknown reason.\n\nError: {Error}\n\nThe system will reboot in {Time}")
        if Time != 0:
            time.sleep(1)
            continue
        os.system("shutdown /r /t 0") 
