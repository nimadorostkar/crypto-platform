from django.urls import path, include
from . import views


urlpatterns = [
    path('source_exchanges', views.SourceExchanges.as_view(), name='source_exchanges'),
    path('user_exchanges', views.UserExchanges.as_view(), name='user_exchanges'),
    path('exchange/<int:id>', views.Exchange.as_view(), name='exchange'),
    path('exchange_data/<int:id>', views.ExchangeData.as_view(), name='exchange_data'),
]
