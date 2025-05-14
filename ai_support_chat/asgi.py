import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from middleware import JWTAuthMiddleware
import chat.routing  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_support_chat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": JWTAuthMiddleware(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})