from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

from MusicServerApp.Device.DeviceAuthTokenSerializer import DeviceAuthTokenSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.
def ofdlkd():
    pass
@api_view(["POST"])
def loginView(request, *args, **kwargs):
    UUID = request.POST.get("UUID")
    password = request.POST.get("password")
    try:
        device = authenticate(username=UUID,
                              password=password)
    except:
        device = None
    if not device:
        return Response({
            "user_not_found": "There is no user \
            with this UUID and password !"
        })
    token = Token.objects.get(user=UUID)
    return Response({
        "token": token.key,
    })