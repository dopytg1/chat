import asyncio
import websockets
import json


async def client():
    async with websockets.connect('ws://localhost:5000', ping_interval=None) as websocket:
        while True:
            data = json.loads(await websocket.recv())
            print("{}: {}".format(data["name"].strip(), data["message"]))

asyncio.get_event_loop().run_until_complete(client())
