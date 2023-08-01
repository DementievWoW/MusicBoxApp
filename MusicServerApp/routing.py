from django.template.defaulttags import url
from django.urls import path, re_path

from MusicServerApp import DeviceConsumer
from MusicServerApp.DeviceConsumer import DeviceConsumer

websocket_urlpatterns = [
    re_path("ws", DeviceConsumer.as_asgi())
]
