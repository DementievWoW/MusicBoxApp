from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from MusicServerApp.models import Device

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy

from rest_framework import serializers


class DeviceAuthTokenSerializer(serializers.Serializer):
    UUID = serializers.UUIDField(label=gettext_lazy("UUID"))
    password = serializers.CharField(
        label=gettext_lazy("Password", ),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        UUID = attrs.get('UUID')
        password = attrs.get('password')

        if UUID and password:
            device = authenticate(request=self.context.get('request'),
                                  UUID=UUID, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not device:
                msg = gettext_lazy('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = gettext_lazy('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['device'] = device
        return attrs
