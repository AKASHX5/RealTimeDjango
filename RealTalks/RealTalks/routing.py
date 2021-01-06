from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import RealTalks.convo.routing



application = ProtocolTypeRouter(
    {
        "websocket":AuthMiddlewareStack(
            URLRouter(
                RealTalks.convo.routing.websocket_urlpatterns
            )
        ),
        "http": get_asgi_application(),

    }
)