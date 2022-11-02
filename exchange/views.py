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

        """
        An alternative way to import:
        from pybit.inverse_perpetual import WebSocket, HTTP
        """

        # Set up logging (optional)
        import logging
        logging.basicConfig(filename="pybit.log", level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")


        # Connect with authentication!
        ws_inverse = inverse_perpetual.WebSocket(
            test=True,
            api_key=api_key,  # omit the api_key & secret to connect w/o authentication
            api_secret=api_secret,
            # to pass a custom domain in case of connectivity problems, you can use:
            domain="bytick"  # the default is "bybit"
        )

        # Let's fetch the orderbook for BTCUSD. First, we'll define a function.
        def handle_orderbook(message):
            # I will be called every time there is new orderbook data!
            print(message)
            orderbook_data = message["data"]

        # Now, we can subscribe to the orderbook stream and pass our arguments:
        # our function and our selected symbol.
        # To subscribe to multiple symbols, pass a list: ["BTCUSD", "ETHUSD"]
        # To subscribe to all symbols, pass "*".
        ws_inverse.orderbook_25_stream(handle_orderbook, "BTCUSD")


        # To subscribe to private data, the process is the same:
        def handle_position(message):
            # I will be called every time there is new position data!
            print(message)

        ws_inverse.position_stream(handle_position)


        # Similarly, if you want to listen to the WebSockets of other markets:
        ws_spot = spot.WebSocket(test=True)
        # handle_orderbook() will now be called for both inverse and spot data.
        # To keep the data separate, simply create another function and pass it below.
        ws_spot.depth_v2_stream(handle_orderbook, "BTCUSDT")


        while True:
            # This while loop is required for the program to run. You may execute
            # additional code for your trading logic here.
            sleep(1)
        print('----------')






#
