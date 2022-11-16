import asyncio
import websockets
import json 
from concurrent.futures import ThreadPoolExecutor

name = input("Your name: ")

async def ainput(prompt: str = ''):
    with ThreadPoolExecutor(1, 'ainput') as executor:
        return (await asyncio.get_event_loop().run_in_executor(executor, input, prompt)).rstrip()

async def client():
    async with websockets.connect('ws://localhost:5000', ping_interval=None) as websocket:
        while True:
            message = await ainput("")
            await websocket.send(json.dumps({"name": name, "message": message}))
                # print(response)
    

asyncio.get_event_loop().run_until_complete(client())



# def new_connection():
#     choise = input("type: register or login").lower().strip()
#     if choise == "register":
#         username = input("Your username: ")
#         password = input("Your password: ")
#         last_name = input("Your last name: ")
#         first_name = input("Your first name: ")
#     elif choise == "login":
#         username = input("username: ")
#         password = input("password: ")

#     else:
#         print("unknown command")
#         new_connection()

# new_connection()


