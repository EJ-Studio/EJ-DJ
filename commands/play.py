
'''
 ********      **    ********   **               ** **                 
/**/////      /**   **//////   /**              /**//                  
/**           /**  /**        ********   **     /** **  ******   ******
/*******      /**  /*********///**//**  /**  ******/** **////** **//// 
/**////       /**  ////////**  /** /**  /** **///**/**/**   /**//***** 
/**       **  /**         /**  /** /**  /**/**  /**/**/**   /** /////**
/********//*****    ********   //**//******//******/**//******  ****** 
////////  /////    ////////     //  //////  ////// //  //////  //////  '''




'''

 **                                      **        
/**             ******                  /**        
/** ********** /**///** ******  ****** ************
/**//**//**//**/**  /****////**//**//*///**/**//// 
/** /** /** /**/******/**   /** /** /   /**//***** 
/** /** /** /**/**/// /**   /** /**     /** /////**
/** *** /** /**/**    //****** /***     //******** 
// ///  //  // //      //////  ///       ////////  '''



import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import os
from os import system
from packages.CRITICAL.CLIENT import client
from commands.data import FOOTER, BOT_CHANNELS
import asyncio
import subprocess
import urllib.request
import re #regular expression
from shutil import copyfile
import random

#IMPORTS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''

   ********  **          **               **        
  **//////**/**         /**              /**        
 **      // /**  ****** /**      ******  /**  ******
/**         /** **////**/****** //////** /** **//// 
/**    *****/**/**   /**/**///** ******* /**//***** 
//**  ////**/**/**   /**/**  /****////** /** /////**
 //******** ***//****** /******//*********** ****** 
  //////// ///  //////  /////   /////////// //////  '''#########################################################################################################################################################################


global url
url = ""

global radio
radio = False

global playlist
playlist = False

global previous_song_1
previous_song_1 = ""
global previous_song_2
previous_song_2 = ""

global WAITING_FOR_DOWNLOAD
WAITING_FOR_DOWNLOAD = False

#GLOBAL^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''

 *******  **                 
/**////**/**          **   **
/**   /**/**  ****** //** ** 
/******* /** //////** //***  
/**////  /**  *******  /**   
/**      /** **////**  **    
/**      ***//**********     
//      ///  //////////      '''################################################################################################################################################################################################



@client.command(pass_context=True, aliases=['p', 'Play'])
async def play(ctx, *, url ):#, url):
    if ctx.channel.name in BOT_CHANNELS.channels:

        try:
            if ctx.voice_client is None: #This should check if the bot is connected to a voice channel.
                channel = ctx.author.voice.channel
                await channel.connect()

                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="",
                    description=f"Joined channel preparing to play!\nPlease read >info.")
                update = await ctx.send(embed = update_embed)
                await asyncio.sleep(5)
                await update.delete()
            else:
                pass
                # update_embed = discord.Embed(
                #     colour=discord.Colour.gold(),
                #     title="",
                #     description=f"Already joined this channel.")
                # await ctx.send(embed = update_embed)
        except Exception as Error:
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description=f"You are not in a voice channel.")
            await ctx.send(embed = update_embed)
            return

        global radio
        try:
            if radio == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Cannot perform this action while radio is playing.")
                await ctx.send(embed = update_embed)
                return
            else:
                pass

        except:
            pass

        global playlist
        try:
            if playlist == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Cannot perform this action while playlist is playing.")
                await ctx.send(embed = update_embed)
                return
            else:
                pass

        except:
            pass
        while WAITING_FOR_DOWNLOAD == True:
            pass
        try:
            global voice
            if voice == voice:
                pass
        except Exception as Error:
            voice = get(client.voice_clients, guild=ctx.guild)

        #print(url)
        if "https://" not in url:
            await ctx.message.delete()

            url = url.replace(" ", "+")
            #print(url)
            html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url}")
            #print(html.read().decode())
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            #print(video_ids[0])
            url = f"https://www.youtube.com/watch?v={video_ids[0]}"

            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(url, download=False) 
                song_name = (meta['title'])

            update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="",
            description=f"Added song: {song_name}")

            await ctx.send(embed = update_embed)

        else:
            await ctx.message.delete()
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(url, download=False) 
                song_name = (meta['title'])

            update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="",
            description=f"Added song: {song_name}")

            await ctx.send(embed = update_embed)

            #print(url)
            #https://www.youtube.com/watch?v=fN1Cyr0ZK9M
            #https://www.youtube.com/results?search_query=heello+their
            # query = os.system('youtube_dl -g ytsearch5:python 3 ')
            # print(query)
            #https://www.youtube.com/watch?v=IDGOESHERE

        
        try:#CHECKS IF RETRIES EXISTS, pretty much.
            if retries == "":
                retries = 0
        except:
            retries = 0
        ## try:
        ##     if retries == "":
        ##         retries = 0
        ##         pass
        ##     else:
        ##         if retries == 1:
        ##             pass
        ## except:
        ##     retries = 0

        try:
            global queue_info
            if queue_info != []:
                pass
            else:
                queue_info = []
            queue_info.append(url)
            #await ctx.send(queue_info)
        except:
            queue_info = [url]
            #await ctx.send(queue_info)
            #return

        while voice.is_playing():
            return

        else:
            await playsong(ctx, queue_info[0], retries)
            #pass

async def playsong(ctx, url, retries):

    print("Someone wants to play music let me get that ready for them...")
    voice = get(client.voice_clients, guild=ctx.guild)
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
            global now_playing_url
            now_playing_url = url


            ydl_opts = {}#{"outtmpl": path}
            with youtube_dl.YoutubeDL(ydl_opts) as yd:
                meta = yd.extract_info(url, download=False) 
                song_name = (meta['title'])
                song_duration = (meta['duration'])

                if '"' in song_name:
                    print('An " was detected within the songs name.')
                    #song_name = file[:-12]
                    song_name = song_name.replace('"', "")
                    print(f'Replaced the ' )
                if "|" in song_name:
                    song_name = song_name.replace("|", "_")

            #print(song_duration)

            if song_duration <= 599:
                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="",
                    description=f"Preparing song: {song_name}")

                preparing_embed = await ctx.send(embed = update_embed)
                #possible_file = f"./cached_songs/{song_name}.mp3"
                if os.path.isfile(rf'./cached_songs/{song_name}.mp3'):
                    song_dir = f"./cached_songs/{song_name}.mp3"

                    await preparing_embed.delete()

                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Playing now: {song_name}")
                    await ctx.send(embed = update_embed)
                    pass
                    
                else:
                    WAITING_FOR_DOWNLOAD = True
                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Please wait as your song downloads <a:loading:768429190193086475>")
                    sent = await ctx.send(embed = update_embed)
                    song_dir = ()
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
                        return

                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Playing now: {song_name}")
                    await ctx.send(embed = update_embed)

            elif song_duration >= 600:
                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="",
                    description=f"Cant play song because it is : {(round((song_duration)/60))} minutes long.")

                await ctx.send(embed = update_embed)
                queue_info.remove(url)
                now_playing_url = []
                song_dir = ()
                return

            # elif song_duration <= 599:
            #     update_embed = discord.Embed(
            #         colour=discord.Colour.green(),
            #         title="",
            #         description=f"Preparing song: {song_name}")

            #     await ctx.send(embed = update_embed)
            #     ydl.download([url])


            #ydl.download([url])
        except:
            try:
                print(retries)
                if retries == 1:
                    retries = 0
                    queue_info.remove(url)

                    update_embed = discord.Embed(
                        colour=discord.Colour.red(),
                        title="",
                        description=f"Could not resolve the issue, skipping song.")

                    await ctx.send(embed = update_embed)

                    print("REMOVED URL BECUASE OF ERROR<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    if queue_info != []:
                        await playsong(ctx, queue_info[0], retries)
                else:
                    update_embed = discord.Embed(
                        colour=discord.Colour.red(),
                        title="",
                        description=f"Sorry something went wrong while attempting to play this song. Retrying...")

                    await ctx.send(embed = update_embed)

                    #await ctx.send("Sorry something went wrong, we will retry once!")
                    retries = 1
                    await playsong(ctx, queue_info[0], retries)
            except Exception as Error:
                print(Error)
                update_embed = discord.Embed(
                    colour=discord.Colour.red(),
                    title="",
                    description=f"Sorry something went wrong while attempting to play this song. Retrying...")

                await ctx.send(embed = update_embed)
                #await ctx.send("Sorry something went wrong, we will retry once!")
                retries = 1
                await playsong(ctx, queue_info[0], retries)
            #ydl.search([url])

    if song_dir == ():
        global file
        for file in os.listdir("./"):
            if file.endswith(".mp3"):

                voice.play(discord.FFmpegPCMAudio(file))#, after= my_after(url))

                queue_info.remove(url)
                WAITING_FOR_DOWNLOAD = False
                print("REMOVED URL<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

                while True:
                    if not voice.is_playing(): #if the voice isnt playing.
                        if not voice.is_paused(): #if the music isnt paused
                            try:
                                
                                retries = 0
                                for file in os.listdir("./"):
                                    if file.endswith(".mp3"):
                                        try:
                                            print(file)
                                            print(song_name)
                                            os.rename(file, f'{song_name}.mp3')
                                            if os.path.isfile(f'./cached_songs/{song_name}.mp3'):
                                                pass
                                            else:
                                                try:
                                                    copyfile(f"./{song_name}.mp3", f"./cached_songs/{song_name}.mp3")
                                                except Exception as Error:
                                                    print("died here because: ", Error)
                                                pass
                                        except Exception as Error:
                                            print(Error)
                                            pass
                                        os.remove(rf"./{song_name}.mp3")
                                if queue_info != []:
                                    now_playing_url = []
                                    await playsong(ctx, queue_info[0], retries)
                                    return
                                else:
                                    now_playing_url = []
                                    break

                            except Exception as Error:
                                await ctx.send(Error)
                                break #I CHANGED THIS FROM BREAK
                        else:
                            #print("2")
                            await asyncio.sleep(5)
                            continue
                    else:
                        #print("1")
                        await asyncio.sleep(5)
                        continue
    elif song_dir != ():
        voice.play(discord.FFmpegPCMAudio(song_dir))#, after= my_after(url))
        #await ctx.send(queue_info)
        voice.volume = 100

        queue_info.remove(url)
        song_dir = ()
        print("REMOVED URL<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

        while True:
            if not voice.is_playing(): #if the voice isnt playing.
                if not voice.is_paused(): #if the music isnt paused
                    try:
                        retries = 0
                        for file in os.listdir("./"):
                            if file.endswith(".mp3"):
                                try:
                                    os.rename(file, f'{song_name}.mp3')
                                    if os.path.isfile(rf'./cached_songs/{song_name}.mp3'):
                                        pass
                                    else:
                                        try:
                                            copyfile(f"./{song_name}.mp3", f"./cached_songs/{song_name}.mp3")
                                        except Exception as Error:
                                            print("died here because: ", Error)
                                        pass
                                except Exception as Error:
                                    print(Error)
                                    break
                                os.remove(f"./{song_name}.mp3")
                        if queue_info != []:
                            now_playing_url = []
                            await playsong(ctx, queue_info[0], retries)
                            return
                        else:
                            now_playing_url = []
                            break

                    except Exception as Error:
                        await ctx.send(Error)
                        break
                else:
                    #print("2")
                    await asyncio.sleep(5)
                    continue
            else:
                #print("1")
                await asyncio.sleep(5)
                continue


#PLAY^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''

  ******** **     **        
 **////// /**    //  ****** 
/**       /**  ** **/**///**
/*********/** ** /**/**  /**
////////**/****  /**/****** 
       /**/**/** /**/**///  
 ******** /**//**/**/**     
////////  //  // // //      '''#################################################################################################################################################################################################

#THE >skip COMMAND
@client.command(pass_context=True, aliases=["s", "Skip", "stop", "Stop"])
async def skip(ctx):#, url):
    if ctx.channel.name in BOT_CHANNELS.channels:

        try:
            global radio
            if radio == True:
                voice.stop()
                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="",
                    description="Skipping to next song.")
                await ctx.send(embed = update_embed)
                return
        except:
            pass

        try:
            global playlist
            if playlist == True:
                voice.stop()
                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="",
                    description="Skipping to next song.")
                await ctx.send(embed = update_embed)
                return
        except:
            pass

        try:
            voice.stop()
            
            #NEW V0.1.5
            if queue_info == []:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description=f"Their are no songs in your queue.")
                await ctx.send(embed = update_embed)

            else:
                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="",
                    description=f"Skipping song.")
                await ctx.send(embed = update_embed)
            #-----------------------------
            await asyncio.sleep(5)
            return
        except:
            print("OOF")
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description=f"No music is playing...")

            await ctx.send(embed = update_embed)
            return
            #await ctx.send("Music isnt playing.")

        #queue_info.remove(url)
        print("REMOVED URL BECUASE OF SKIP OVERIDE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        if queue_info == []:
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description=f"Their are no songs in your queue.")

            await ctx.send(embed = update_embed)

#SKIP^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


'''

   *******                                   
  **/////**                                  
 **     //**  **   **  *****  **   **  ***** 
/**      /** /**  /** **///**/**  /** **///**
/**    **/** /**  /**/*******/**  /**/*******
//**  // **  /**  /**/**//// /**  /**/**//// 
 //******* **//******//******//******//******
  /////// //  //////  //////  //////  ////// '''################################################################################################################################################################################

#THE queue COMMAND!
@client.command(pass_context=True, aliases=["q", "Queue"])
async def queue(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        global radio
        global playing_radio

        if radio == True:
            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="",
                description=f"Loading queue please wait <a:loading:768429190193086475>")
            sent = await ctx.send(embed = update_embed)

            pfp = client.user.avatar_url

            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="QUEUE",
                description="MODE: Radio")

            update_embed.set_author(name="EJ DJ", icon_url=(pfp))
            update_embed.set_thumbnail(url=(pfp))

            update_embed.add_field(name="Currently playing:", value=f"{playing_radio}", inline=True)

            await sent.delete()
            await ctx.send(embed = update_embed)
            return

        elif playlist == True:
            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="",
                description=f"Loading queue please wait <a:loading:768429190193086475>")
            sent = await ctx.send(embed = update_embed)

            pfp = client.user.avatar_url

            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="QUEUE",
                description="MODE: Playlist")

            update_embed.set_author(name="EJ DJ", icon_url=(pfp))
            update_embed.set_thumbnail(url=(pfp))

            update_embed.add_field(name="Currently playing:", value=f"{playing_playlist}", inline=True)

            await sent.delete()
            await ctx.send(embed = update_embed)
            return


        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="",
            description=f"Loading queue please wait <a:loading:768429190193086475>")
        sent = await ctx.send(embed = update_embed)

        pfp = client.user.avatar_url

        update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="QUEUE",
            description="MODE: Normal")

        update_embed.set_author(name="EJ DJ", icon_url=(pfp))
        update_embed.set_thumbnail(url=(pfp))

        try:
            if now_playing_url != []:
                ydl_opts = {}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    meta = ydl.extract_info(now_playing_url, download=False) 
                    song_name = (meta['title'])
                update_embed.add_field(name="Currently playing:", value=f"{song_name}", inline=True)
            else:
                update_embed.add_field(name="Currently playing:", value="No song Currently playing.", inline=True)
        except Exception as Error:
            print(Error)
            update_embed.add_field(name="Currently playing:", value="No song Currently playing.", inline=True)

        try:
            for number in range(len(queue_info)):
                up_next = queue_info[number]
                ydl_opts = {}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    meta = ydl.extract_info(up_next, download=False) 
                    song_name = (meta['title'])
                    if number == 0:
                        update_embed.add_field(name="Up next:", value=f"{song_name}", inline=True)
                    else:
                        update_embed.add_field(name=f"{number} | Up next:", value=f"{song_name}", inline=True)

            update_embed.set_footer(text=f"{FOOTER.footer}")
            await sent.delete()
            await ctx.send(embed = update_embed)
            return
        except:
            update_embed.add_field(name="Up next:", value="No song Currently in queue.", inline=True)
            update_embed.set_footer(text=f"{FOOTER.footer}")
            await sent.delete()
            await ctx.send(embed = update_embed)
            return

#QUEUE^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^








'''

   ******  **                         
  **////**/**                         
 **    // /**  *****   ******   ******
/**       /** **///** //////** //**//*
/**       /**/*******  *******  /** / 
//**    **/**/**////  **////**  /**   
 //****** ***//******//********/***   
  ////// ///  //////  //////// ///    '''######################################################################################################################################################################################


#THE >clear COMMAND
@client.command(pass_context=True, aliases=["c", "Clear"])
async def clear(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        if queue_info != []:
            queue_info.clear()

            update_embed = discord.Embed(
            colour=discord.Colour.green(),
            title="",
            description="Cleared the queue.")

            await ctx.send(embed = update_embed)

        else:
            update_embed = discord.Embed(
            colour=discord.Colour.gold(),
            title="",
            description="No songs in the queue.")

            await ctx.send(embed = update_embed)

#CLEAR^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^








'''

 *******                  ** **         
/**////**                /**//          
/**   /**   ******       /** **  ****** 
/*******   //////**   ******/** **////**
/**///**    *******  **///**/**/**   /**
/**  //**  **////** /**  /**/**/**   /**
/**   //**//********//******/**//****** 
//     //  ////////  ////// //  //////  '''##################################################################################################################################################################################

@client.command(pass_context=True, aliases=["r", "Radio"])
async def radio(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        global radio
        global playing_radio
        global voice
        global playlist

        try:
            if playlist == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Cannot perform this action while playlist is playing.")
                await ctx.send(embed = update_embed)
                return
            else:
                pass

        except:
            pass

        try:
            if ctx.voice_client is None: #This should check if the bot is connected to a voice channel.
                channel = ctx.author.voice.channel
                await channel.connect()

                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="",
                    description=f"Joined channel preparing to play!")
                update = await ctx.send(embed = update_embed)

                await update.delete()

            else:
                ##channel = ctx.author.voice.channel
                ##await channel.connect()
                pass

        except Exception as Error:
            print(Error)
            if radio == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="The radio is already going.")
                await ctx.send(embed = update_embed)
                return
                
            elif voice.is_playing():
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Cannot perform this action while playing music.")
                await ctx.send(embed = update_embed)
                return

            elif voice.is_paused():
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Cannot perform this action while paused.")
                await ctx.send(embed = update_embed)
                return

            else:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description=f"You are not in a voice channel.")
                await ctx.send(embed = update_embed)
                return

        
        try:
            if radio == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="The radio is already going.")
                await ctx.send(embed = update_embed)
                return
            elif radio == False:
                pass
        except:
            pass


        try:
            if voice == voice:
                pass
        except Exception as Error:
            voice = get(client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description="Cannot perform this action while playing music.")
            await ctx.send(embed = update_embed)
            return
        elif voice.is_paused():
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description="Cannot perform this action while paused.")
            await ctx.send(embed = update_embed)
            return
        else:
            print("set radio to True")
            radio = True
            playing_radio = ()
            while True:
                try:
                    if radio == True:
                        if voice.is_playing():
                            await asyncio.sleep(5)
                            continue
                        elif voice.is_paused():
                            await asyncio.sleep(5)
                            continue
                        else:
                            path = r"./cached_songs/"
                            songs = []
                            for song in os.listdir(path):
                                songs += [song]
                            play1 = random.choices(songs)
                            play = rf"./cached_songs/{play1[0]}"
                            voice.play(discord.FFmpegPCMAudio(play))

                            play1 = ((play1[0]).replace(".mp3", ""))
                            playing_radio = play1
                            update_embed = discord.Embed(
                                colour=discord.Colour.green(),
                                title="",
                                description=f"Type `stop radio` to stop the radio\nNow playing: {play1}")
                            sent = await ctx.send(embed = update_embed)
                            await asyncio.sleep(5)
                            await sent.delete()
                            continue
                    else:
                        return
                except Exception as Error:
                    print(Error)

                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Please wait as the radio re-initializes.")
                    alert = await ctx.send(embed = update_embed)

                    await ctx.voice_client.disconnect()

                    channel = ctx.author.voice.channel
                    await channel.connect()
                    #RECONNECTING

                    voice = get(client.voice_clients, guild=ctx.guild)

                    await alert.delete()
                        
                    continue

#RADIO^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




'''

 *******                  ** **                 *******  **                  ** **          **              **                  
/**////**                /**//                 /**////**/**          **   **/**//          /**             /**           ****** 
/**   /**   ******       /** **  ******        /**   /**/**  ****** //** ** /** **  ************    ************ ****** /**///**
/*******   //////**   ******/** **////**       /******* /** //////** //***  /**/** **///////**/    **///////**/ **////**/**  /**
/**///**    *******  **///**/**/**   /**   **  /**////  /**  *******  /**   /**/**//*****  /**    //*****  /** /**   /**/****** 
/**  //**  **////** /**  /**/**/**   /**  //   /**      /** **////**  **    /**/** /////** /**     /////** /** /**   /**/**///  
/**   //**//********//******/**//******    **  /**      ***//**********     ***/** ******  //**    ******  //**//****** /**     
//     //  ////////  ////// //  //////    //   //      ///  //////////     /// // //////    //    //////    //  //////  //      '''########################################################################################


@client.event
async def on_message(message):
    if message.channel.name in BOT_CHANNELS.channels:

        global radio
        global playlist
        if radio == True:
            if "stop radio" in message.content:
                radio = False
                voice.stop()

        elif playlist == True:
            if "stop playlist" in message.content:
                playlist = False
                voice.stop()


        await client.process_commands(message)

#RADIO/ PLAYLIST STOP^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





'''
 **                                       
/**                                       
/**        *****   ******  **    ** ***** 
/**       **///** //////**/**   /****///**
/**      /*******  *******//** /**/*******
/**      /**////  **////** //**** /**//// 
/********//******//******** //**  //******
////////  //////  ////////   //    ////// '''###############################################################################################################################################################################


@client.command(pass_context=True, aliases=["Leave"])
async def leave(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        global radio
        global playlist
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

            if radio == True:
                radio = False
                voice.stop()
                print(radio)

            elif playlist == True:
                playlist = False
                voice.stop()
                print(playlist)

            await ctx.voice_client.disconnect()

#LEAVE^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




'''

 *******           **           **                                             
/**////**         /**          /**                                       ***** 
/**    /**  ***** /**  *****  ****** *****     ******  ******  *******  **///**
/**    /** **///**/** **///**///**/ **///**   **////  **////**//**///**/**  /**
/**    /**/*******/**/*******  /** /*******  //***** /**   /** /**  /**//******
/**    ** /**//// /**/**////   /** /**////    /////**/**   /** /**  /** /////**
/*******  //*********//******  //**//******   ****** //******  ***  /**  ***** 
///////    /////////  //////    //  //////   //////   //////  ///   //  /////  '''##########################################################################################################################################



@client.command(pass_context=True, aliases=["remove", "delete"])
async def delete_song(ctx, *, search=None):
    if ctx.channel.name in BOT_CHANNELS.channels:

        role = discord.utils.get(ctx.guild.roles, name="bot controller")
        if role in ctx.author.roles:
            pass
        else:
            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="",
                description=f"You do not have permission to perform this action.")
            await ctx.send(embed = update_embed)
            return

        global radio
        global playing_radio

        if search == None:
            if radio == True:
                print(f"Deleting {playing_radio}.mp3")
                song = str(playing_radio + ".mp3")

                voice.stop()
                await asyncio.sleep(5)

                path = r"./cached_songs/"

                song_path = str(path + song)

                if os.path.exists(song_path):
                    os.remove(song_path)
                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Removed: {song}")
                    await ctx.send(embed = update_embed)
                    return
                else:
                    update_embed = discord.Embed(
                        colour=discord.Colour.red(),
                        title="",
                        description=f"Could not find {song} in the data base.")
                    await ctx.send(embed = update_embed)
                    return

            else:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description=f"Your not using the radio")
                await ctx.send(embed = update_embed)
                return

        else:
            if "https://" not in search:
                #await ctx.message.delete()

                url = search

                url = url.replace(" ", "+")
                #print(url)
                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url}")
                #print(html.read().decode())
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                #print(video_ids[0])
                url = f"https://www.youtube.com/watch?v={video_ids[0]}"

                ydl_opts = {}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    meta = ydl.extract_info(url, download=False) 
                    song_name = (meta['title'])

                song = str(song_name + ".mp3")
                path = r"./cached_songs/"
                song_path = str(path + song)

                if os.path.exists(song_path):
                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Removing: {song}")
                    sent = await ctx.send(embed = update_embed)

                    os.remove(song_path)

                    await sent.delete()

                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Removed: {song}")
                    await ctx.send(embed = update_embed)
                    return

                else:
                    update_embed = discord.Embed(
                        colour=discord.Colour.gold(),
                        title="",
                        description=f"{song} was not found in the data base.")
                    await ctx.send(embed = update_embed)
                    return


            else:
                url = search

                ydl_opts = {}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    meta = ydl.extract_info(url, download=False) 
                    song_name = (meta['title'])

                song = str(song_name + ".mp3")
                path = r"./cached_songs/"
                song_path = str(path + song)

                if os.path.exists(song_path):
                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Removing: {song}")
                    sent = await ctx.send(embed = update_embed)

                    os.remove(song_path)

                    await sent.delete()

                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Removed: {song}")
                    await ctx.send(embed = update_embed)
                    return

                else:
                    update_embed = discord.Embed(
                        colour=discord.Colour.gold(),
                        title="",
                        description=f"{song} was not found in the data base.")
                    await ctx.send(embed = update_embed)
                    return

#DELETE SONG^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




'''

 **       ** **            
/**      // /**            
/**       **/**  **  ***** 
/**      /**/** **  **///**
/**      /**/****  /*******
/**      /**/**/** /**//// 
/********/**/**//**//******
//////// // //  //  ////// '''################################################################################################################################################################################################



@client.command(pass_context=True, aliases=["Like"])
async def like(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        global radio
        global playing_radio

        print(ctx.author)
        try:
            print(now_playing_url)
        except:
            pass

        if radio == True:
            if os.path.isfile(rf'./commands/data/PROFILES/{ctx.author}.py'):
                path = rf'./commands/data/PROFILES/{ctx.author}.py'
                lines = open(path).read()
                print(lines)
                if (f"{playing_radio}.mp3") in lines:
                    update_embed = discord.Embed(
                        colour=discord.Colour.gold(),
                        title="",
                        description=f"You have already liked this song!")
                    await ctx.send(embed = update_embed)
                    return

                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="LIKED:heart:",
                    description=f"{playing_radio}")
                await ctx.send(embed = update_embed)

                path = r'./commands/data/PROFILES/'
                file = f"{ctx.author}.py"
                with open(os.path.join(path, file), 'a') as fp:
                    fp.write(str(f"{playing_radio}.mp3\n"))
                    fp.close()

            else:
                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="LIKED:heart:",
                    description=f"Welcome {ctx.author} we have created a profile for you and saved {playing_radio} to it!")
                await ctx.send(embed = update_embed)

                path = r'./commands/data/PROFILES/'
                file = f"{ctx.author}.py"
                with open(os.path.join(path, file), 'a') as fp:
                    fp.write(str(f"{playing_radio}.mp3\n"))
                    fp.close()

                #os.mkdir(rf'./commands/data/PROFILES/{ctx.author}.py')
                #then continue to append the song to their name

        else:
            try:
                if now_playing_url != []:
                    ydl_opts = {}
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        meta = ydl.extract_info(now_playing_url, download=False) 
                        song_name = (meta['title'])

                    if os.path.isfile(rf'./commands/data/PROFILES/{ctx.author}.py'):

                        update_embed = discord.Embed(
                            colour=discord.Colour.green(),
                            title="LIKED:heart:",
                            description=f"{song_name}")
                        await ctx.send(embed = update_embed)


                        path = r'./commands/data/PROFILES/'
                        file = f"{ctx.author}.py"
                        with open(os.path.join(path, file), 'a') as fp:
                            fp.write(str(f"{song_name}.mp3\n"))
                            fp.close()
                    else:
                        update_embed = discord.Embed(
                            colour=discord.Colour.green(),
                            title="LIKED:heart:",
                            description=f"Welcome {ctx.author} we have created a profile for you and saved {song_name} to it!")
                        await ctx.send(embed = update_embed)
                        path = r'./commands/data/PROFILES/'
                        file = f"{ctx.author}.py"
                        with open(os.path.join(path, file), 'a') as fp:
                            fp.write(str(f"{song_name}.mp3\n"))
                            fp.close()

                else:
                    update_embed = discord.Embed(
                        colour=discord.Colour.gold(),
                        title="No song?",
                        description=f"You need to have a song playing to like it.")
                    await ctx.send(embed = update_embed)

            except Exception as Error:
                print(Error)
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="No song?",
                    description=f"You need to have a song playing to like it.")
                await ctx.send(embed = update_embed)



@client.command(pass_context=True, aliases=["Unlike"])
async def unlike(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        global radio
        global playing_radio

        global playlist
        global playing_playlist

        print(ctx.author)
        try:
            print(now_playing_url)
        except:
            pass

        if os.path.isfile(rf'./commands/data/PROFILES/{ctx.author}.py'):

            if radio == True:
                path = rf'./commands/data/PROFILES/{ctx.author}.py'
                lines = open(path).read()
                if (f"{playing_radio}.mp3") not in lines:
                    update_embed = discord.Embed(
                        colour=discord.Colour.gold(),
                        title="",
                        description=f"This song is not in your likes...")
                    await ctx.send(embed = update_embed)
                    return

                elif (f"{playing_radio}.mp3") in lines:
                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="UNLIKED",
                        description=f"{playing_radio}")
                    await ctx.send(embed = update_embed)

                    path = rf'./commands/data/PROFILES/{ctx.author}.py'
                    with open(path, "r") as f:
                        lines = f.readlines()
                        with open(path, "w") as f:
                            for line in lines:
                                if line.strip("\n") != f"{playing_radio}.mp3":
                                    f.write(line)

                else:
                    update_embed = discord.Embed(
                        colour=discord.Colour.red(),
                        title="Sorry an error occured",
                        description=f"While checking if this song was in your playlist.")
                    await ctx.send(embed = update_embed)
                    print("CRITICAL: An error has occured under radio in >unlike.")
                    return

            elif playlist == True:
                path = rf'./commands/data/PROFILES/{ctx.author}.py'
                lines = open(path).read()
                if (f"{playing_playlist}.mp3") not in lines:
                    update_embed = discord.Embed(
                        colour=discord.Colour.gold(),
                        title="",
                        description=f"This song is not in your likes...")
                    await ctx.send(embed = update_embed)
                    return

                elif (f"{playing_playlist}.mp3") in lines:
                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="UNLIKED",
                        description=f"{playing_playlist}")
                    await ctx.send(embed = update_embed)

                    path = rf'./commands/data/PROFILES/{ctx.author}.py'
                    with open(path, "r") as f:
                        lines = f.readlines()
                        with open(path, "w") as f:
                            for line in lines:
                                if line.strip("\n") != f"{playing_playlist}.mp3":
                                    f.write(line)

                else:
                    update_embed = discord.Embed(
                        colour=discord.Colour.red(),
                        title="Sorry an error occured",
                        description=f"While checking if this song was in your playlist.")
                    await ctx.send(embed = update_embed)
                    print("CRITICAL: An error has occured under playlist in >unlike.")
                    return

            else:
                try:
                    if now_playing_url != []:
                        ydl_opts = {}
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            meta = ydl.extract_info(now_playing_url, download=False) 
                            song_name = (meta['title'])

                        path = rf'./commands/data/PROFILES/{ctx.author}.py'
                        lines = open(path).read()
                        if (f"{song_name}.mp3") not in lines:
                            update_embed = discord.Embed(
                                colour=discord.Colour.gold(),
                                title="",
                                description=f"This song is not in your likes...")
                            await ctx.send(embed = update_embed)
                            return

                        elif (f"{song_name}.mp3") in lines:
                            update_embed = discord.Embed(
                                colour=discord.Colour.green(),
                                title="UNLIKED",
                                description=f"{song_name}")
                            await ctx.send(embed = update_embed)

                            path = rf'./commands/data/PROFILES/{ctx.author}.py'
                            with open(path, "r") as f:
                                lines = f.readlines()
                                with open(path, "w") as f:
                                    for line in lines:
                                        if line.strip("\n") != f"{song_name}.mp3":
                                            f.write(line)

                    else:
                        update_embed = discord.Embed(
                            colour=discord.Colour.gold(),
                            title="No song?",
                            description=f"You need to have a song playing to like it.")
                        await ctx.send(embed = update_embed)

                except Exception as Error:
                    print(Error)
                    update_embed = discord.Embed(
                        colour=discord.Colour.gold(),
                        title="No song?",
                        description=f"You need to have a song playing to like it.")
                    await ctx.send(embed = update_embed)


@client.command(pass_context=True, aliases=["List"])
async def list(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        global radio
        global playing_radio

        if os.path.isfile(rf'./commands/data/PROFILES/{ctx.author}.py'):
            path = rf'./commands/data/PROFILES/{ctx.author}.py'
            lines = open(path).read()

            update_embed = discord.Embed(
                colour=discord.Colour.green(),
                title="Your liked songs:",
                description=f"{lines}")
            await ctx.send(embed = update_embed)
            return

        else:
            update_embed = discord.Embed(
                colour=discord.Colour.red(),
                title="Sorry...",
                description=f"You dont have a profile.\nPlease read >info under >like to figure out how to make a profile.")
            await ctx.send(embed = update_embed)
            return


#LIKE^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^





'''
*******  **                  ** **          **  
/**////**/**          **   **/**//          /**  
/**   /**/**  ****** //** ** /** **  ************
/******* /** //////** //***  /**/** **///////**/ 
/**////  /**  *******  /**   /**/**//*****  /**  
/**      /** **////**  **    /**/** /////** /**  
/**      ***//**********     ***/** ******  //** 
//      ///  //////////     /// // //////    //  '''#######################################################################################################################################################################




@client.command(pass_context=True, aliases=["profile", "pl"])
async def playlist(ctx):
    if ctx.channel.name in BOT_CHANNELS.channels:

        author = (ctx.author)

        if os.path.isfile(rf'./commands/data/PROFILES/{ctx.author}.py'):
            pass
        else:
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description=f"Sorry, you have no liked songs.")
            await ctx.send(embed = update_embed)
            return


        global playlist
        global playing_playlist
        #voice = get(client.voice_clients, guild=ctx.guild)
        #print(ctx.voice_client)
        global voice

        global radio

        global previous_song_1
        global previous_song_2


        try:
            if radio == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Cannot perform this action while the radio is playing.")
                await ctx.send(embed = update_embed)
                return

            elif Playlist == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Your playlist is already playing.")
                await ctx.send(embed = update_embed)
                return
            else:
                pass

        except:
            pass


        try:
            if ctx.voice_client is None: #This should check if the bot is connected to a voice channel.
                channel = ctx.author.voice.channel
                await channel.connect()

                update_embed = discord.Embed(
                    colour=discord.Colour.green(),
                    title="",
                    description=f"Joined channel preparing to play!")
                update = await ctx.send(embed = update_embed)

                await update.delete()

            else:
                pass

        except Exception as Error:
            print(Error)
            if playlist == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="The playlist is already going.")
                await ctx.send(embed = update_embed)
                return
                
            elif voice.is_playing():
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Cannot perform this action while playing music.")
                await ctx.send(embed = update_embed)
                return

            elif voice.is_paused():
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="Cannot perform this action while paused.")
                await ctx.send(embed = update_embed)
                return

            else:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description=f"You are not in a voice channel.")
                await ctx.send(embed = update_embed)
                return

        
        try:
            if playlist == True:
                update_embed = discord.Embed(
                    colour=discord.Colour.gold(),
                    title="",
                    description="The playlist is already going.")
                await ctx.send(embed = update_embed)
                return
            elif playlist == False:
                pass
        except:
            pass

        # radio = True
        # playing_radio = ()

        try:
            #global voice
            if voice == voice:
                pass
        except Exception as Error:
            voice = get(client.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description="Cannot perform this action while playing music.")
            await ctx.send(embed = update_embed)
            return
        elif voice.is_paused():
            update_embed = discord.Embed(
                colour=discord.Colour.gold(),
                title="",
                description="Cannot perform this action while paused.")
            await ctx.send(embed = update_embed)
            return
        else:
            print("set playlist to True")
            playlist = True
            playing_playlist = ()

            while True:
                try:
                    if playlist == True:
                        if voice.is_playing():
                            await asyncio.sleep(5)
                            continue
                        elif voice.is_paused():
                            await asyncio.sleep(5)
                            continue
                        else:
                            path = rf'./commands/data/PROFILES/{ctx.author}.py'
                            retry = 0
                            while True:
                                try:
                                    lines = open(path).read().splitlines()
                                    song = random.choice(lines)
                                    pass
                                except:
                                    update_embed = discord.Embed(
                                        colour=discord.Colour.gold(),
                                        title="",
                                        description=f"Sorry, you have no liked songs.")
                                    await ctx.send(embed = update_embed)
                                    playlist = False
                                    return

                                if song == previous_song_1 or song == previous_song_2:
                                    retry += 1
                                    if retry == 5:
                                        retry = 0
                                        break
                                    else:
                                        continue

                                else:
                                    previous_song_2 = previous_song_1
                                    previous_song_1 = song
                                    break
                                    
                            print(song)

                            play1 = song #random.sample(songs, 1)
                            #print(play1)
                            play = rf"./cached_songs/{play1}"
                            voice.play(discord.FFmpegPCMAudio(play))

                            play1 = ((play1).replace(".mp3", ""))
                            playing_playlist = play1
                            update_embed = discord.Embed(
                                colour=discord.Colour.green(),
                                title="",
                                description=f"Type `stop playlist` to stop your playlist\nNow playing: {play1}")
                            sent = await ctx.send(embed = update_embed)
                            await asyncio.sleep(5)
                            await sent.delete()
                            continue

                            # except Exception as Error:
                            #     if Error == "Not connected to voice.":
                            #         print(Error)

                            #         update_embed = discord.Embed(
                            #             colour=discord.Colour.green(),
                            #             title="",
                            #             description=f"Please wait re-initializing.")
                            #         alert = await ctx.send(embed = update_embed)
                            #         await ctx.voice_client.disconnect()
                            #         channel = ctx.author.voice.channel
                            #         await channel.connect()
                            #         #RECONNECTING
                            #         voice = get(client.voice_clients, guild=ctx.guild)
                            #         await alert.delete()
                            #         continue

                            #     elif Error == "Cannot choose from an empty sequence":
                            #         print(Error)
                            #         update_embed = discord.Embed(
                            #             colour=discord.Colour.gold(),
                            #             title="",
                            #             description=f"Sorry, you have no liked songs.")
                            #         await ctx.send(embed = update_embed)
                            #         playlist = False
                            #         return

                                # else:
                                #     print("CRITICAL:" + str(Error))
                                #     #print(Error)

                                #     update_embed = discord.Embed(
                                #         colour=discord.Colour.green(),
                                #         title="",
                                #         description=f"Please wait re-initializing.")
                                #     alert = await ctx.send(embed = update_embed)
                                #     await ctx.voice_client.disconnect()
                                #     channel = ctx.author.voice.channel
                                #     await channel.connect()
                                #     #RECONNECTING
                                #     voice = get(client.voice_clients, guild=ctx.guild)
                                #     await alert.delete()
                                #     continue

                    else:
                        return

                except Exception as Error:
                    print(Error)

                    update_embed = discord.Embed(
                        colour=discord.Colour.green(),
                        title="",
                        description=f"Please wait re-initializing.")
                    alert = await ctx.send(embed = update_embed)

                    await ctx.voice_client.disconnect()

                    channel = ctx.author.voice.channel
                    await channel.connect()
                    #RECONNECTING

                    voice = get(client.voice_clients, guild=ctx.guild)

                    await alert.delete()
                        
                    continue

#PLAYLIST^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^