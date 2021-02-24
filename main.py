import requests
import hmac
import hashlib
import time

URL = "https://testnet.binancefuture.com/"
API = "/fapi/v1/openOrders"
TIME_API = "/fapi/v1/time"
API_KEY = "56971583e9834ae35380da085357bba22a223524ae5c9a77b81543a58f3ac872"
API_SECRET = "ba19d7ebd0eeb3f8f81d70851be6dde7a6e0800c8aee434ed4a87295d96d7370"
time_request = requests.get(url=URL+TIME_API)
current_time = time_request.json()["serverTime"]

message = 'timestamp='+str(current_time)
signature = hmac.new(
    bytes(API_SECRET , 'latin-1'),
    msg = bytes(message , 'latin-1'),
    digestmod=hashlib.sha256
).hexdigest()#.upper()
#print(str(signature))
open_orders = requests.get( url=URL+API, params = {'timestamp' : str(current_time) , 'signature': str(signature)} , headers={'X-MBX-APIKEY': str(API_KEY)})
print(open_orders.json())