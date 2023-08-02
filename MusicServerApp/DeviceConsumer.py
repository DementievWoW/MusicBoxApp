import logging

from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from pyasn1.debug import scope

from MusicServerApp import DeviceSerializer
from MusicServerApp.models import Device
import uuid

clients = {}


class DeviceConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        global clients
        await self.send("Подключение прошло успешно")

    async def disconnect(self, code):
        await self.send("Устройство отключено")
        await self.close()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        logging.info(text_data)

    # async def receive_json(self, content, **kwargs):
    #     # Called with either text_data or bytes_data for each frame
    #     # You can call:
    #     logging.info("receive_json"+content)
    #     await self.send(text_data="Hello world!")

# clients = {}

# class DeviceConsumer(AsyncWebsocketConsumer):
# class DeviceConsumer(WebsocketConsumer):
#     # queryset = Device.id
#     # serializer_class = DeviceSerializer
#
#     async def connect(self):
#         # logging.debug("подключение 1")
#         # global clients
#         # await self.close()
#         # self.accept()
#         # clients[self.scope["user"]] = self.channel_name
#         self.accept()
#         self.send(text_data="ifjfk")
#         self.room_name = self.scope['url_route']
#         # await self.send(text_data="dkfmvclldkc")
#         # await self.send(bytes_data="dkfmvclldkc")
#
#     async def disconnect(self, code):
#         logging.debug("отключение 1")
