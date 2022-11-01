from django.contrib import admin
from .models import Exchange, SourceExchange, TradeType



#-------------------------------------------------------------------------------
class TradeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(TradeType, TradeTypeAdmin)


#-------------------------------------------------------------------------------
class SourceExchangeAdmin(admin.ModelAdmin):
    list_display = ('logo_img', 'name', 'smart_trade', 'dca_bot', 'grid_bot', 'options_bot')
admin.site.register(SourceExchange, SourceExchangeAdmin)



#-------------------------------------------------------------------------------
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'exchange' , 'status', 'created_at')
    list_filter = ('status', 'created_at', 'exchange', 'user')
    search_fields = ['name', 'user__username']
    raw_id_fields = ('user'),
admin.site.register(Exchange, ExchangeAdmin)
