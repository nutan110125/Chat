# mysite/routing.py
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import *

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<sender>[0-9]+)/(?P<receiver>[0-9]+)$', ChatConsumer),
]


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})