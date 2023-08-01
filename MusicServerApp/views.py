from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import DeviceSerializer
from .models import Device

# Create your views here.

class DeviceAPIView(APIView):
    def get(self, request):
        lst = Device.objects.all().values()
        return Response({'MusicBox': list(lst)})

    def post(self, request):
        title = request.data['physicalСores']
        content = request.data['totalCores']
        return Response(f"{title} : {content}")
