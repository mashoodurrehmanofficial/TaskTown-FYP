# chat_app/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path,re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # path('ws/chat/', ChatConsumer.as_asgi()),
       re_path(r'ws/chat/(?P<project_id>\d*)/$', ChatConsumer.as_asgi()),


]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
