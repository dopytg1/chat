import asyncio
import websockets
import json 

all_clients = []

async def send_message(message):
    for websocket in all_clients:
        print(message)
        await websocket.send(json.dumps(message))
    await asyncio.sleep(2)


async def new_client_connected(client_socket, path):
    print("New client connected")
    all_clients.append(client_socket)
    print(client_socket)

    while True:
        data = json.loads(await client_socket.recv())
        context = {
            "name": data["name"],
            "message": data["message"]
        }
        print(data)
        await send_message(context)

async def start_server():
    await websockets.serve(new_client_connected, "localhost", 5000, ping_interval=None)


if __name__ == "__main__":
    try:
        event__loop = asyncio.get_event_loop()
        event__loop.run_until_complete(start_server())
        event__loop.run_forever()
    except websockets.ConnectionClosed as e:
        print(f'Terminated', e)
