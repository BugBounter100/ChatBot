#!/usr/bin/env python

# WS client example

import asyncio
import websockets

while(True):
	async def hello():
	    uri = "ws://localhost:8765"
	    async with websockets.connect(uri) as websocket:
	        name = input("User Input ")
	        print(f"Start messaging with the bot (type BHAAG to stop)!")

	        await websocket.send(name)
	        # print(f"> {name}")

	        greeting = await websocket.recv()
	        print(f" ChatBot --> {greeting}")

	asyncio.get_event_loop().run_until_complete(hello())