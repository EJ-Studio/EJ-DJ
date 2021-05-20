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
import random
from PIL import Image, ImageDraw, ImageFont
import urllib.request
import io
from discord import File


@client.event
async def on_member_join(ctx):

    AVATAR_SIZE = 128

    # --- duplicate image ----

    background_image = Image.open("pic.png").convert("RGBA")

    image = background_image.copy()

    image_width, image_height = image.size

    # --- draw on image ---

    # create object for drawing

    #draw = ImageDraw.Draw(image)

    # draw red rectangle with alpha channel on new image (with the same size as original image)

    rect_x0 = 20  # left marign
    rect_y0 = 20  # top marign

    rect_x1 = image_width - 20  # right margin
    rect_y1 = 20 + AVATAR_SIZE - 1  # top margin + size of avatar

    rect_width  = rect_x1 - rect_x0
    rect_height = rect_y1 - rect_y0

    rectangle_image = Image.new('RGBA', (image_width, image_height))
    rectangle_draw = ImageDraw.Draw(rectangle_image)

    rectangle_draw.rectangle((rect_x0, rect_y0, rect_x1, rect_y1), fill=(0, 255, 128, 128))

    # put rectangle on original image

    image = Image.alpha_composite(image, rectangle_image)

    # create object for drawing

    draw = ImageDraw.Draw(image) # create new object for drawing after changing original `image`

    # draw text in center

    text = f'Welcome to MatrixCraft\n{ctx.name}\nMember #:{ctx.guild.member_count}'

    #font = ImageFont.truetype('Arial.ttf', 30)
    font = ImageFont.truetype("arial.ttf", 28, encoding="unic")


    text_width, text_height = draw.textsize(text, font=font)
    x = (rect_width - text_width - AVATAR_SIZE)//2     # skip avatar when center text
    y = (rect_height - text_height)//2

    x += rect_x0 + AVATAR_SIZE     # skip avatar when center text
    y += rect_y0

    draw.text((x, y), text, fill=(0,0,0,0), font=font)

    # --- avatar ---

    # get URL to avatar
    # sometimes `size=` doesn't gives me image in expected size so later I use `resize()`
    avatar_asset = ctx.avatar_url_as(format='jpg', size=AVATAR_SIZE)

    # read JPG from server to buffer (file-like object)
    buffer_avatar = io.BytesIO()
    await avatar_asset.save(buffer_avatar)
    buffer_avatar.seek(0)

    # read JPG from buffer to Image
    avatar_image = Image.open(buffer_avatar)

    # resize it
    avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE)) #

    #image.paste(avatar_image, (rect_x0, rect_y0))
    circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
    circle_draw = ImageDraw.Draw(circle_image)
    circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)

    image.paste(avatar_image, (rect_x0, rect_y0), circle_image)

    # --- sending image ---

    # create buffer
    buffer_output = io.BytesIO()

    # save PNG in buffer
    image.save(buffer_output, format='PNG')

    # move to beginning of buffer so `send()` it will read from beginning
    buffer_output.seek(0)

    # send image
    channel = client.get_channel(657348370502778893)
    await channel.send(file=File(buffer_output, 'myimage.png'))