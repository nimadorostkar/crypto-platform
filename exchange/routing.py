from django.urls import path
from exchange import consumers

websocket_urlpatterns = [
    path('exchange_test', consumers.ExchangeConsumer.as_asgi()),
]
