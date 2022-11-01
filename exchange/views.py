from .models import Exchange
from . import models
from .serializers import ExchangeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, filters, status, pagination, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from pybit import inverse_perpetual




#--------------------------------------------------- UserExchanges -------------
class UserExchanges(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.filter(user=request.user)
        serializer = ExchangeSerializer(exchange, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=request.data
        data['user']=request.user.id
        serializer = ExchangeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







#-------------------------------------------------------- Exchange -------------
class Exchange(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])
        serializer = ExchangeSerializer(exchange)
        return Response(serializer.data, status=status.HTTP_200_OK)






#---------------------------------------------------- ExchangeData -------------
class ExchangeData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])

        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=exchange.api_key, api_secret=exchange.api_secret)
        ws = inverse_perpetual.WebSocket(test=False, api_key=exchange.api_key, api_secret=exchange.api_secret)

        # Get orderbook.
        session.orderbook(symbol='BTCUSD')

        # Create five long orders.
        orders = [{
            "symbol": "BTCUSD",
            "order_type": "Limit",
            "side": "Buy",
            "qty": 100,
            "price": i,
            "time_in_force": "GoodTillCancel"
        } for i in [5000, 5500, 6000, 6500, 7000]]

        # Submit the orders in bulk.
        session.place_active_order_bulk(orders)

        # Check on your order and position through WebSocket.
        def handle_orderbook(message):
            print(message)
        def handle_position(message):
            print(message)

        ws.orderbook_25_stream(handle_orderbook, "BTCUSD")
        ws.position_stream(handle_position)

        while True:
            # Run your main trading strategy here
            pass  # To avoid CPU utilisation, use time.sleep(1)

        return Response(status=status.HTTP_200_OK)





#
