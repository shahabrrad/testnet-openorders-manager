import asyncio
import websockets
import json
import requests
import hmac
import hashlib

URL = "https://testnet.binancefuture.com/"
API = "/fapi/v1/listenKey"
TIME_API = "/fapi/v1/time"



API_KEY = "56971583e9834ae35380da085357bba22a223524ae5c9a77b81543a58f3ac872"
API_SECRET = "ba19d7ebd0eeb3f8f81d70851be6dde7a6e0800c8aee434ed4a87295d96d7370"

time_request = requests.get(url=URL+TIME_API)
current_time = time_request.json()["serverTime"]

message = ''
signature = hmac.new(
    bytes(API_SECRET , 'latin-1'),
    msg = bytes(message , 'latin-1'),
    digestmod=hashlib.sha256
).hexdigest()#.upper()
    #print(str(signature))
open_orders = requests.post( url=URL+API, params = {'signature': str(signature)} , headers={'X-MBX-APIKEY': str(API_KEY)})



print(open_orders.json())
listenkey = open_orders.json()['listenKey']

# Launch the connection to the server.

async def hello():
    async with websockets.connect('wss://stream.binancefuture.com/ws/'+str(listenkey)) as websocket:
        while True:
            result = await websocket.recv()
            print(json.loads(result))

asyncio.get_event_loop().run_until_complete(hello())