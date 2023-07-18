from django.db import models

import os
from uuid import uuid1


class Device(models.Model):
    class Meta:
        db_table = 'Device'
        verbose_name = 'Музыкальный аппарат'
        verbose_name_plural = 'Музыкальные аппараты'

    def get_StartedLogs_path(self, filename):
        result = os.path.join('DeviceLogs/StartedLogs/', str(self.id), uuid1().hex, '%Y/%m/%d/%H/%M/%S')
        if '.' in filename:
            result = os.path.join(result, filename.split('.')[-1])
        return result

    def get_RunTimeLogs_path(self, filename):
        result = os.path.join('DeviceLogs/StartedLogs/', str(self.id), uuid1().hex, '%Y/%m/%d/%H/%M/%S')
        if '.' in filename:
            result = os.path.join(result, filename.split('.')[-1])
        return result

    id = models.UUIDField(primary_key=True)
    namePlace = models.TextField(verbose_name="Место нахождения", blank=False)
    timeCreate = models.DateTimeField(verbose_name='Время создания',
                                      blank=False,
                                      auto_now_add=True)
    timeUpdate = models.DateTimeField(verbose_name='Время последнего обновления',
                                      blank=False,
                                      auto_now=True)
    startedLogsPath = models.FileField(
        verbose_name='Путь к логам старта',
        upload_to=get_StartedLogs_path,
        blank=False,

    )

    runTimeLogs = models.FileField(
        verbose_name='Путь к логам работы',
        upload_to=get_RunTimeLogs_path,
        blank=False,

    )
    sentСommands = models.OneToOneField('sentСommands',
                                        verbose_name='Принятые команды',
                                        on_delete=models.PROTECT,
                                        null=True)
    statusData = models.OneToOneField("statusData",
                                      verbose_name='информация по состоянию устройства',
                                      on_delete=models.PROTECT,
                                      null=True)


class statusData(models.Model):
    class Meta:
        db_table = 'statusData'
        verbose_name = 'информация по состоянию устройства'

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class sentСommands(models.Model):
    class Meta:
        db_table = 'sentСommands'
        verbose_name = 'отправленная команда'
        verbose_name_plural = 'отправленные команды'

    id = models.UUIDField(primary_key=True)
    commandType = models.ForeignKey('commandType',
                                    verbose_name="Тип команды",
                                    on_delete=models.PROTECT,
                                    null=True)
    timeCreate = models.DateTimeField(verbose_name='Время отправки команды',
                                      blank=False,
                                      auto_now_add=True)

    def __str__(self):
        return f'{self.commandType.name} {self.timeCreate}'


class commandType(models.Model):
    class Meta:
        db_table = 'commandType'
        verbose_name = 'Тип команды'
        verbose_name_plural = 'Типы команд'

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
