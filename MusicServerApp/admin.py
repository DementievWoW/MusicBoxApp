import logging

import channels.layers
from asgiref.sync import async_to_sync
from django.contrib import admin
from django.db.models import QuerySet

from .models import Device, RuntimeLogs, StatusData, StartLogs
from channels.layers import get_channel_layer


@admin.register(Device)
class Device(admin.ModelAdmin):
    list_display = ('id', 'namePlace', 'timeCreate', 'timeUpdate')
    readonly_fields = ('id', 'statusData', 'timeCreate', 'timeUpdate')
    fields = ('id', 'namePlace', 'Password', 'timeCreate', 'timeUpdate', 'statusData',)
    actions = ['reloadDevice']

    def statusData(self, obj):
        stri = ""
        for item in StatusData.objects.filter(Device_id=obj.id):
            stri += f"\n" + str(item) + "\n"
        return stri

