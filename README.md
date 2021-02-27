
# testnet-openorders-manager
A web based program to manage open orders of binance test-net
There are some errors as of right now.

I used normal API to get orders list and was planning to use websockets to later alter the list on webpage. To do so, I used websockets package to recieve changes from binance stream. Then, I used channels package to create a stream from my backend to frontend. I didn't do it directly from front to binance api because I need hmac sha256 to creat a stream and doing that in js seems a bit too much.

The error that I get now is that I call consumer.send inside an async function to recieve from binance stream.
curently working on it.
The only problem rght now is that pages do not update themselves automatically.

------------------------------------------------------

UPDATE:

I used another solution by sending ListenKey from view to js in index.html and then creating a websocket connection there and managing it there. I don't know how safe this is. Also we won't be able to monitor and log the change of  orders list in the backend but I don't know if that is our goal so I hope it is ok.