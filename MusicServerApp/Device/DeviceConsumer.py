import json
import logging

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from urllib.parse import parse_qs
from MusicServerApp.models import Device, CommandType
import uuid
#
# devices = {}


class DeviceConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        try:
            query_string = self.scope["query_string"]
            query_params = query_string.decode()
            query_dict = parse_qs(query_params)
            UUID = uuid.UUID(query_dict['UUID'][0]).hex
            device: Device = await getDataBaseDeviceObject(UUID)
            if device.Password == query_dict['password'][0] and str(device.pk) == query_dict['UUID'][0]:
                # await self.channel_layer.group_add(
                #     'Device',
                #     self.channel_name,
                # )
                # global devices
                # devices[UUID] = self
                # await self.accept()

                await self.send("Подключение прошло успешно")
                logging.info(f"Устройство {device.id} c адреса {self.scope['client']} подключено ")
            else:
                await self.close()
                logging.info(f"Устройство {device.id} c адреса {self.scope['client']} не смогло подключиться ")
            # global clients
        except:
            logging.error(f"Устройство {self.scope['client']} не смогло подключиться")

    async def disconnect(self, code):
        await self.send("Устройство отключено")
        # await self.channel_layer.group_discard(
        #     'Device',
        #     self.channel_name
        # )
        # for k, v in devices.items():
        #     if v == self.channel_name:
        #         del devices[self.channel_name]
        # await self.close()
        logging.info(f"Устройство {self.scope['client']} отключено")

    async def receive_json(self, content, **kwargs):
        device: Device = await getDataBaseDeviceObject(uuid.UUID(content["UUID"]).hex)
        await createRuntimeLogs(device, content['RuntimeLogs'])
        await createStartLogs(device, content['StartLogs'])
        await createStatusData(device, content['machineState'])


@database_sync_to_async
def getDataBaseDeviceObject(pk: uuid.UUID) -> Device:
    try:
        return Device.objects.get(pk=pk)
    except:
        logging.error("В методе getDataBaseDeviceObject произошла ошибка")


@database_sync_to_async
def createStatusData(device: Device, statusData: list):
    try:
        device.statusdata_set.create(
            physicalСores=statusData[0]["physicalСores"],
            totalCores=statusData[0]["totalCores"],
            frequencyMax=statusData[0]["frequencyMax"],
            frequencyMin=statusData[0]["frequencyMin"],
            frequencyСurrent=statusData[0]["frequencyСurrent"],
            cpuPercent=statusData[0]["cpuPercent"],
            cpuPercentForCore=statusData[0]["cpuPercentForCore"],
            totalSizeMemory=statusData[0]["totalSizeMemory"],
            availableSizeMemory=statusData[0]["availableSizeMemory"],
            usedSizeMemory=statusData[0]["usedSizeMemory"],
            percentMemory=statusData[0]["percentMemory"],
            totalSizeSwapMemory=statusData[0]["totalSizeSwapMemory"],
            freeSizeSwapMemory=statusData[0]["freeSizeSwapMemory"],
            usedSizeSwapMemory=statusData[0]["usedSizeSwapMemory"],
            percentSwapMemory=statusData[0]["percentSwapMemory"],
            diskInfo=statusData[0]["diskInfo"],
            webInfo=statusData[0]["webInfo"],
            webByteSent=statusData[0]["webByteSent"],
            webByteRecv=statusData[0]["webByteRecv"],
            # температура только для linux
            temp=statusData[0]["temp"],
            timeCreateMSK=statusData[0]["timeCreateMSK"],
        )
    except:
        logging.error("В методе CreateStatusData произошла ошибка")


async def createStartLogs(device: Device, startlogsList: list):
    # тут не @database_sync_to_async, потому что синхронным должно быть только обращение к бд, что бы
    # пока идет цикл другие методы могли работать с бд
    try:
        for startLog in startlogsList:
            for item in startLog.values():
                await database_sync_to_async(device.startlogs_set.create)(
                    MsgType=item[0],
                    DateMsg=item[1],
                    Msg=item[2]
                )
    except:
        logging.error("в методе CreateStartLogs произошла ошибка")


async def createRuntimeLogs(device: Device, runtimeList: list):
    # тут не @database_sync_to_async, потому что синхронным должно быть только обращение к бд, что бы
    # пока идет цикл другие методы могли работать с бд
    try:
        for runtimeLog in runtimeList:
            for item in runtimeLog.values():
                await database_sync_to_async(device.runtimelogs_set.create)(
                    DateMsg=item[0],
                    Msg=item[1]
                )
    except:
        logging.error("в методе CreateRuntimeLogs произошла ошибка")