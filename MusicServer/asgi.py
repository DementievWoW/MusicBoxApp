"""
ASGI config for MusicServer project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

import django
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MusicServer.settings')
django.setup()
from MusicServerApp import routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )

    # "websocket": JwtAuthMiddlewareStack(
    #     URLRouter(
    #         routing.websocket_urlpatterns
    #     )
    # )
})
# application = get_asgi_application()
