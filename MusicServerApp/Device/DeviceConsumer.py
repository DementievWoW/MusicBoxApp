import logging

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

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

    async def receive_json(self, content, **kwargs):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        logging.info("receive_json")
        logging.info("UUID")
        logging.info(uuid.UUID(content["UUID"]).hex)
        # logging.info(content)
        # logging.info()
        logging.info(content["machineState"][0]["physicalСores"])
        device: Device = await self.getDataBaseDeviceObject(uuid.UUID(content["UUID"]).hex)
        await database_sync_to_async(device.statusdata_set.create)(
            name=f'Status data by Device: {content["UUID"]}',
            physicalСores=content["machineState"][0]["physicalСores"],
            totalCores=content["machineState"][0]["totalCores"],
            frequencyMax=content["machineState"][0]["frequencyMax"],
            frequencyMin=content["machineState"][0]["frequencyMin"],
            frequencyСurrent=content["machineState"][0]["frequencyСurrent"],
            cpuPercent=content["machineState"][0]["cpuPercent"],
            cpuPercentForCore=content["machineState"][0]["cpuPercentForCore"],
            totalSizeMemory=content["machineState"][0]["totalSizeMemory"],
            availableSizeMemory=content["machineState"][0]["availableSizeMemory"],
            usedSizeMemory=content["machineState"][0]["usedSizeMemory"],
            percentMemory=content["machineState"][0]["percentMemory"],
            totalSizeSwapMemory=content["machineState"][0]["totalSizeSwapMemory"],
            freeSizeSwapMemory=content["machineState"][0]["freeSizeSwapMemory"],
            usedSizeSwapMemory=content["machineState"][0]["usedSizeSwapMemory"],
            percentSwapMemory=content["machineState"][0]["percentSwapMemory"],
            diskInfo=content["machineState"][0]["diskInfo"],
            webInfo=content["machineState"][0]["webInfo"],
            webByteSent=content["machineState"][0]["webByteSent"],
            webByteRecv=content["machineState"][0]["webByteRecv"],
            # температура только для linux
            temp=content["machineState"][0]["temp"],
            timeCreateMSK=content["machineState"][0]["timeCreateMSK"],
        )
        # device.statusData_set.add(statusDataObject, bulk=False)
        logging.info(device)

    @database_sync_to_async
    def getDataBaseDeviceObject(self, pk: uuid.UUID) -> Device:
        # logging.info(Device.objects.get(uuid.UUID(id).hex))
        return Device.objects.get(pk=pk)

    # logging.info(content)

    # async def receive(self, text_data=None, bytes_data=None, **kwargs):
    #     logging.info("receive text" + text_data)
    #     logging.info(bytes_data)

    # @action()
    # # async def machineState(self, text_data=None):

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
