from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer, \
                                       AsyncWebsocketConsumer
import json
import asyncio
import time


class EchoConsumer(AsyncConsumer):

    # async specifies that this code should be run on a separate thread
    # This is an abstract method which is called when a
    # client connects to this socket
    async def websocket_connect(self, event):
        # await is a blocking call within this thread
        # send json with type 'websocket.accept' to accept connection
        await self.send({
            "type": "websocket.accept",
            "data": "websocket connected"
        })

    async def websocket_receive(self, event):
        # Echo the payload received from client
        text_data_json = json.loads(event)
        message = text_data_json['data']

        await self.send({
            "type": "on receive",
            "data": message
        })


# Here we send and recieve string. The api is much simpler
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # accept connection
        self.accept()
        # send the data in any format as a string
        self.send(json.dumps({
            "type": "on connect",
            "data": "websocket connected"
        }))
        # For next 10 seconds the server wont respond for recieved msgs
        time.sleep(10)
        # self.close()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['data']

        self.send(json.dumps({
            "type": "on receive",
            "data": message
        }))


# Here we send and recieve string. The api is much simpler
class AsyncChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # accept connection
        await self.accept()
        # send the data in any format as a string
        await self.send(json.dumps({
            "type": "on connect",
            "data": "websocket connected"
        }))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['data']

        await self.send(json.dumps({
            "type": "on receive",
            "data": message
        }))


class AnotherAsyncChatConsumer(AsyncChatConsumer):
        async def connect(self):
            super.connect()
            # For next 10 seconds the server wont respond for recieved msgs
            await asyncio.sleep(10)
            print("Hi")
            await self.send(json.dumps({
                "type": "on connect",
                "data": "10 seconds over"
            }))
