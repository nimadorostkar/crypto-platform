from rest_framework import serializers
from .models import Exchange, SourceExchange, TradeType



class TradeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeType
        fields = '__all__'


class SourceExchangeSerializer(serializers.ModelSerializer):
    order_types = TradeTypeSerializer(read_only=True, many=True)
    class Meta:
        model = SourceExchange
        fields = '__all__'


class ExchangeSerializer(serializers.ModelSerializer):
    #exchange = SourceExchangeSerializer(read_only=True)
    class Meta:
        model = Exchange
        fields = '__all__'
