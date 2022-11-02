import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from exchange.consumers import ExchangeConsumer

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')



application = ProtocolTypeRouter({

   "http": get_asgi_application(),
   "websocket": URLRouter([
        path('exchange_test', ExchangeConsumer.as_asgi())
     ])
})
