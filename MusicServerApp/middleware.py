from channels.middleware import BaseMiddleware
from django.db import close_old_connections


class TokenAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        close_old_connections()


def JwtAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(inner)
