from django.db import models


class Device(models.Model):
    class Meta:
        db_table = 'Device'
        verbose_name = 'Музыкальный аппарат'
        verbose_name_plural = 'Музыкальные аппараты'

    id = models.UUIDField(primary_key=True)
    Password = models.TextField(verbose_name="Пароль", blank=True)
    namePlace = models.TextField(verbose_name="Место нахождения", blank=False)
    timeCreate = models.DateTimeField(verbose_name='Время создания',
                                      blank=False,
                                      auto_now_add=True)
    timeUpdate = models.DateTimeField(verbose_name='Время последнего обновления',
                                      blank=False,
                                      auto_now=True)
    def __str__(self):
        return f' Place: {self.namePlace}; UUID {self.id};'

class RuntimeLogs(models.Model):
    class Meta:
        db_table = 'Runtime Logs'
        verbose_name = 'Логи работы машины'

    Device = models.ForeignKey(Device,
                               verbose_name='Девайс',
                               on_delete=models.PROTECT,
                               null=True,
                               blank=True)
    DateMsg = models.TextField(verbose_name="Время создания события", blank=True)
    Msg = models.TextField(verbose_name="Сообщение события", blank=True)
    def __str__(self):
        return f'{self.DateMsg} {self.Msg}'

class StartLogs(models.Model):
    class Meta:
        db_table = 'StartedLogs'
        verbose_name = 'Логи старта машины'

    Device = models.ForeignKey(Device,
                               verbose_name='Девайс',
                               on_delete=models.PROTECT,
                               null=True,
                               blank=True)
    MsgType = models.TextField(verbose_name="Тип сообщения", blank=True)
    DateMsg = models.TextField(verbose_name="Время создания события", blank=True)
    Msg = models.TextField(verbose_name="Сообщение события", blank=True)
    def __str__(self):
        return f'{self.MsgType} {self.DateMsg} {self.Msg}'
class StatusData(models.Model):
    class Meta:
        db_table = 'statusData'
        verbose_name = 'информация по состоянию устройства'
        verbose_name_plural = 'информация по состоянию устройства'

    Device = models.ForeignKey(Device,
                               verbose_name='Девайс',
                               on_delete=models.PROTECT,
                               null=True,
                               blank=True)

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
    timeCreateMSK = models.DateTimeField(verbose_name='Время создания отчета на машине',
                                         blank=False)

    def __str__(self):

        return f"Физические ядра: {self.physicalСores} \n" \
               f"Всего ядер: {self.totalCores}\n" \
               f"Максимальная частота:  {self.frequencyMax} \n " \
               f"Минимальная частота: {self.frequencyMin} \n " \
               f"Текущая частота: {self.frequencyСurrent} \n " \
               f"процент использования процессора: {self.cpuPercent} \n" \
               f"процент использования процессора на ядро: {self.cpuPercentForCore} \n" \
               f"общий объем памяти : { self.totalSizeMemory} \n" \
               f"доступный объем памяти : {self.availableSizeMemory} \n" \
               f"используемый размер памяти   : {self.usedSizeMemory} \n" \
               f"процент памяти : {self.percentMemory} \n" \
               f"общий размер подкачиваемой памяти   : {self.totalSizeSwapMemory} \n" \
               f"доступно памяти подкачки  : {self.freeSizeSwapMemory} \n" \
               f"используемый размер подкачки памяти : {self.usedSizeSwapMemory} \n" \
               f"процент подкачки памяти : {self.percentSwapMemory} \n" \
               f"информация о диске/ах : {self.diskInfo} \n" \
               f"информация о сети : {self.webInfo} \n" \
               f"Сеть, байт отправлено : {self.webByteSent} \n" \
               f"Сеть, байт принято :  {self.webByteRecv } \n  " \
               f"Текущая температура : {self.temp} \n       " \
               f"Время создания отчета на машине : {self.timeCreateMSK} \n "


class SentСommands(models.Model):
    class Meta:
        db_table = 'sentСommands'
        verbose_name = 'отправленная команда'
        verbose_name_plural = 'отправленные команды'
    Device = models.ForeignKey(Device,
                                     verbose_name='отправленная команда',
                                     on_delete=models.PROTECT,
                                     null=True,
                                     blank=True)

    id = models.UUIDField(primary_key=True)

    timeCreate = models.DateTimeField(verbose_name='Время отправки команды',
                                      blank=False,
                                      auto_now_add=True)

    def __str__(self):
        return f'{self.commandType.name} {self.timeCreate}'


class CommandType(models.Model):
    class Meta:
        db_table = 'commandType'
        verbose_name = 'Тип команды'
        verbose_name_plural = 'Типы команд'
    sentСommands = models.ForeignKey(SentСommands,
                                    verbose_name="Тип команды",
                                    on_delete=models.PROTECT,
                                    null=True)
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
