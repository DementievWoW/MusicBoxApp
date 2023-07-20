from django.db import models


class Device(models.Model):
    class Meta:
        db_table = 'Device'
        verbose_name = 'Музыкальный аппарат'
        verbose_name_plural = 'Музыкальные аппараты'

    id = models.UUIDField(primary_key=True)
    namePlace = models.TextField(verbose_name="Место нахождения", blank=False)
    timeCreate = models.DateTimeField(verbose_name='Время создания',
                                      blank=False,
                                      auto_now_add=True)
    timeUpdate = models.DateTimeField(verbose_name='Время последнего обновления',
                                      blank=False,
                                      auto_now=True)
    startedLogs = models.TextField(verbose_name="логи старта", blank=False)

    runTimeLogs = models.TextField(verbose_name="логи работы", blank=False)

    sentСommands = models.OneToOneField('sentСommands',
                                        verbose_name='отправленная команда',
                                        on_delete=models.PROTECT,
                                        null=True,
                                        blank=True)
    statusData = models.OneToOneField("statusData",
                                      verbose_name='информация по состоянию устройства',
                                      on_delete=models.PROTECT,
                                      null=True,
                                      blank=True)


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
