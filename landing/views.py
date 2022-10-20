from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from itertools import chain
from rest_framework import viewsets, filters, status, pagination, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
import json
from pybit import inverse_perpetual






API_KEY = '9oWXNBo4Nl2fp8MqG8'
API_SECRET = 'F0L9IbuZTycnP5sy5Nk5ZubUCH9q3urFPrp6'



#------------------------------------------------------ Test -------------------
class Test(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        # Create an HTTP session and connect via WebSocket for Inverse on mainnet:
        session = inverse_perpetual.HTTP(endpoint='https://api.bybit.com', api_key=API_KEY, api_secret=API_SECRET)
        ws = inverse_perpetual.WebSocket(test=False, api_key=API_KEY, api_secret=API_SECRET )


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

        # https://pypi.org/project/pybit/#installation

        return Response(status=status.HTTP_200_OK)















#End
