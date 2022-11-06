from django.urls import path, include
from . import views


urlpatterns = [
    path('source_exchanges', views.SourceExchanges.as_view(), name='source_exchanges'),
    path('user_exchanges', views.UserExchanges.as_view(), name='user_exchanges'),
    path('exchange/<int:id>', views.Exchange.as_view(), name='exchange'),
    path('exchange_data/<int:id>', views.ExchangeData.as_view(), name='exchange_data'),
    #
    path('orderbook/<int:id>', views.OrderBook.as_view(), name='orderbook'),
    path('info_symbol/<int:id>', views.InfoSymbol.as_view(), name='info_symbol'),
    path('query_symbol/<int:id>', views.QuerySymbol.as_view(), name='query_symbol'),
    path('wallet_balance/<int:id>', views.WalletBalance.as_view(), name='wallet_balance'),
    path('active_order/<int:id>', views.ActiveOrder.as_view(), name='active_order'),
    path('my_position/<int:id>', views.MyPosition.as_view(), name='my_position'),
    path('api_key_info/<int:id>', views.ApiKeyInfo.as_view(), name='api_key_info'),
]
