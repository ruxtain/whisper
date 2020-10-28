#!/home/michael/anaconda3/bin/python

import asyncio
import websockets

async def hello():
    uri = "ws://172.17.150.194:8765"
    async with websockets.connect(uri) as websocket:
        name = "002|||robot|||hello world"

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
