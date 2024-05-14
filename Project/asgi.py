import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import app_dashboard.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(
        URLRouter(
            app_dashboard.routing.websocket_urlpatterns
        )
    ),
})
