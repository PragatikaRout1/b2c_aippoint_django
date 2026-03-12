"""
ASGI config for resume_parser_mongodb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import resume_parser.routing  # Import the routing of your app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_parser_mongodb.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            resume_parser.routing.websocket_urlpatterns
        )
    ),
})
