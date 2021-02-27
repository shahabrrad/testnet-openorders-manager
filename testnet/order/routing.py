from django.urls import path
from .consumers import WSconsumer, WSconsumer2

ws_urlpatterns = [
    path('ws/slave1/' , WSconsumer.as_asgi()),
    path('ws/slave2/' , WSconsumer2.as_asgi())
]