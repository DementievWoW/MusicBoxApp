from django.urls import re_path

from MusicServerApp.Device.DeviceConsumer import DeviceConsumer

websocket_urlpatterns = [
    re_path("ws", DeviceConsumer.as_asgi())
]
