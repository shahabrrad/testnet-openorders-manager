from channels.generic.websocket import WebsocketConsumer
import json
import random
from time import sleep
import asyncio
import websockets
import requests
import hmac
import hashlib

def get_listenkey (api_key , api_secret):

    URL = "https://testnet.binancefuture.com/"
    API = "/fapi/v1/listenKey"
    TIME_API = "/fapi/v1/time"
    print("key")
    time_request = requests.get(url=URL+TIME_API)
    current_time = time_request.json()["serverTime"]

    message = ''
    signature = hmac.new(
        bytes(api_secret , 'latin-1'),
        msg = bytes(message , 'latin-1'),
        digestmod=hashlib.sha256
    ).hexdigest()

    key_response = requests.post( url=URL+API, params = {'signature': str(signature)} , headers={'X-MBX-APIKEY': str(api_key)})
    listenkey = key_response.json()['listenKey']

    return listenkey

    



class WSconsumer(WebsocketConsumer):
    def connect(self):
        self.accept()


        API_KEY = "56971583e9834ae35380da085357bba22a223524ae5c9a77b81543a58f3ac872"
        API_SECRET = "ba19d7ebd0eeb3f8f81d70851be6dde7a6e0800c8aee434ed4a87295d96d7370"
        listenkey = get_listenkey(API_KEY , API_SECRET)
        



        async def hello(self):
            print("hello")
            async with websockets.connect('wss://stream.binancefuture.com/ws/'+str(listenkey)) as websocket:
               while True:
                    result = await websocket.recv()
                    order_update = json.loads(result)
                    print(order_update)
                    if order_update['e'] == "ORDER_TRADE_UPDATE":
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        try:
                            loop.run_until_complete(self.send(order_update))
                        except:
                            print ("cannot send here")

        #asyncio.get_event_loop().run_until_complete(hello())
 
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(hello(self))

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        print(text_data)
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:

    def disconnect(self, close_code):
        # Called when the socket closes
        pritn('disconnected')




class WSconsumer2(WebsocketConsumer):
    def connect(self):
        self.accept()


        API_KEY = "2fb8ceaa5ab5e40eda867e6fb00eaced855c92b7c0f50a63601cb1b43a9d3698"
        API_SECRET = "08ff49d5336aa26cedcc0ee342d251fd5ec9f02d7b85db3b4701fd4d979f6c92"
        listenkey = get_listenkey(API_KEY , API_SECRET)
        



        async def hello(self):
            print("hello")
            async with websockets.connect('wss://stream.binancefuture.com/ws/'+str(listenkey)) as websocket:
               while True:
                    result = await websocket.recv()
                    order_update = json.loads(result)
                    print(order_update)
                    if order_update['e'] == "ORDER_TRADE_UPDATE":
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        try:
                            loop.run_until_complete(self.send(order_update))
                        except:
                            print ("cannot send here")

        #asyncio.get_event_loop().run_until_complete(hello())
 
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(hello(self))

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        print(text_data)
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:

    def disconnect(self, close_code):
        # Called when the socket closes
        pritn('disconnected')