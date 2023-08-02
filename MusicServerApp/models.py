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
    physicalСores = models.TextField(verbose_name="Физические ядра", blank=True)
    totalCores = models.TextField(verbose_name="Всего ядер", blank=True)
    frequencyMax = models.TextField(verbose_name="Максимальная частота", blank=True)
    frequencyMin = models.TextField(verbose_name="Минимальная частота", blank=True)
    frequencyСurrent = models.TextField(verbose_name="Текущая частота", blank=True)
    cpuPercent = models.TextField(verbose_name="процент использования процессора", blank=True)
    cpuPercentForCore = models.TextField(verbose_name="процент использования процессора на ядро", blank=True)
    totalSizeMemory = models.TextField(verbose_name="общий объем памяти", blank=True)
    availableSizeMemory = models.TextField(verbose_name="доступный объем памяти", blank=True)
    usedSizeMemory = models.TextField(verbose_name="используемый размер памяти", blank=True)
    percentMemory = models.TextField(verbose_name="процент памяти", blank=True)
    totalSizeSwapMemory = models.TextField(verbose_name="общий размер подкачиваемой памяти", blank=True)
    freeSizeSwapMemory = models.TextField(verbose_name="доступно памяти подкачки", blank=True)
    usedSizeSwapMemory = models.TextField(verbose_name="используемый размер подкачки памяти", blank=True)
    percentSwapMemory = models.TextField(verbose_name="процент подкачки памяти", blank=True)
    diskInfo = models.TextField(verbose_name="информация о диске/ах", blank=True)
    webInfo = models.TextField(verbose_name="информация о сети", blank=True)
    webByteSent = models.TextField(verbose_name="Сеть, байт отправлено ", blank=True)
    webByteRecv = models.TextField(verbose_name="Сеть, байт принято", blank=True)
    # температура только для linux
    temp = models.TextField(verbose_name="Текущая температура", blank=True)
    timeCreate = models.DateTimeField(verbose_name='Время создания',
                                      blank=True,
                                      auto_now_add=True)


    def __str__(self):
        return f'{self.name} {self.timeCreate}'


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
