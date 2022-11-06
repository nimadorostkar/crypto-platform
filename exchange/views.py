from .models import Exchange, SourceExchange
from . import models
from .serializers import ExchangeSerializer, SourceExchangeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, filters, status, pagination, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect

from time import sleep
# Import your desired markets from pybit
from pybit import inverse_perpetual
from pybit import spot

import ccxt



#------------------------------------------------- SourceExchanges -------------
class SourceExchanges(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        exchange = models.SourceExchange.objects.all()
        serializer = SourceExchangeSerializer(exchange, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



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
        api_key=exchange.api_key
        api_secret=exchange.api_secret

        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=api_key, api_secret=api_secret)
        #orderbook = session.orderbook(symbol='BTCUSD')
        #info_symbol = session.latest_information_for_symbol(symbol='BTCUSD')
        #query_symbol = session.query_symbol()
        #wallet_balance = session.get_wallet_balance(coin="BTC")
        #active_order = session.get_active_order(symbol='BTCUSD')
        #my_position = session.my_position()
        #api_key_info = session.api_key_info()

        return Response(orderbook, status=status.HTTP_200_OK)










#---------------------------------------------------- OrderBook -------------
class OrderBook(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])
        api_key=exchange.api_key
        api_secret=exchange.api_secret
        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=api_key, api_secret=api_secret)
        orderbook = session.orderbook(symbol='BTCUSD')
        return Response(orderbook, status=status.HTTP_200_OK)



#---------------------------------------------------- InfoSymbol -------------
class InfoSymbol(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])
        api_key=exchange.api_key
        api_secret=exchange.api_secret
        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=api_key, api_secret=api_secret)
        info_symbol = session.latest_information_for_symbol(symbol='BTCUSD')
        return Response(info_symbol, status=status.HTTP_200_OK)


#---------------------------------------------------- QuerySymbol -------------
class QuerySymbol(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])
        api_key=exchange.api_key
        api_secret=exchange.api_secret
        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=api_key, api_secret=api_secret)
        query_symbol = session.query_symbol()
        return Response(query_symbol, status=status.HTTP_200_OK)


#---------------------------------------------------- WalletBalance -------------
class WalletBalance(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])
        api_key=exchange.api_key
        api_secret=exchange.api_secret
        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=api_key, api_secret=api_secret)
        wallet_balance = session.get_wallet_balance(coin="BTC")
        return Response(wallet_balance, status=status.HTTP_200_OK)



#---------------------------------------------------- ActiveOrder -------------
class ActiveOrder(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])
        api_key=exchange.api_key
        api_secret=exchange.api_secret
        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=api_key, api_secret=api_secret)
        active_order = session.get_active_order(symbol='BTCUSD')
        return Response(active_order, status=status.HTTP_200_OK)



#---------------------------------------------------- MyPosition -------------
class MyPosition(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])
        api_key=exchange.api_key
        api_secret=exchange.api_secret
        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=api_key, api_secret=api_secret)
        my_position = session.my_position()
        return Response(my_position, status=status.HTTP_200_OK)






#---------------------------------------------------- ApiKeyInfo -------------
class ApiKeyInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        exchange = models.Exchange.objects.get(id=self.kwargs["id"])
        api_key=exchange.api_key
        api_secret=exchange.api_secret
        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=api_key, api_secret=api_secret)
        api_key_info = session.api_key_info()
        return Response(my_position, status=status.HTTP_200_OK)





#
