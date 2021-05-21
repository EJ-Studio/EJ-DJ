has_connected = False

@BOT.event
async def on_connect():
    if has_connected:
        await on_reconnect()
    else:
        has_connected = True


async def on_reconnect():
   ...