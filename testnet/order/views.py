from django.shortcuts import render
from django.http import HttpResponse
import requests
import hmac
import hashlib
import time
from django.shortcuts import redirect

URL = "https://testnet.binancefuture.com/"
API = "/fapi/v1/openOrders"
TIME_API = "/fapi/v1/time"

def get_listenkey (api_key , api_secret):
    API = "/fapi/v1/listenKey"
    message = ''
    signature = hmac.new(
        bytes(api_secret , 'latin-1'),
        msg = bytes(message , 'latin-1'),
        digestmod=hashlib.sha256
    ).hexdigest()

    key_response = requests.post( url=URL+API, params = {'signature': str(signature)} , headers={'X-MBX-APIKEY': str(api_key)})
    listenkey = key_response.json()['listenKey']

    return listenkey


# Create your views here.
def index1(request):
    #return HttpResponse("hello")

    API_KEY = "56971583e9834ae35380da085357bba22a223524ae5c9a77b81543a58f3ac872"
    API_SECRET = "ba19d7ebd0eeb3f8f81d70851be6dde7a6e0800c8aee434ed4a87295d96d7370"

    if request.user.username == "slave2" :
        return redirect('/order/slave2/')


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

    listenkey = get_listenkey(API_KEY , API_SECRET)
    

    context = {
        'title' : "slave1",
        'orderlist' : open_orders.json(),
        'listenkey' : listenkey,
    }

    return render(request , "order/index.html" , context)




def index2(request):
    #return HttpResponse("hello")

    API_KEY = "2fb8ceaa5ab5e40eda867e6fb00eaced855c92b7c0f50a63601cb1b43a9d3698"
    API_SECRET = "08ff49d5336aa26cedcc0ee342d251fd5ec9f02d7b85db3b4701fd4d979f6c92"

    if request.user.username == "slave1":
        return redirect('/order/slave1/')


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

    listenkey = get_listenkey(API_KEY , API_SECRET)
    
    context = {
        'title' : "slave2",
        'orderlist' : open_orders.json(),
        'listenkey' : listenkey
    }

    return render(request , "order/index.html" , context)


def master_view(request):
        if request.user.username == "slave1":
            return redirect('/order/slave1/')
        if request.user.username == "slave2" :
            return redirect('/order/slave2/')
        return render(request , "order/master.html")



def landing(request):
    username = request.user.username
    if username == "slave1":
        response = redirect('/order/slave1/')
    if username == "slave2":
        response = redirect('/order/slave2/')
    if username == "slavemaster":
        response = redirect('/order/master/')
    return response