from django.contrib import admin
from .models import Exchange


#-------------------------------------------------------------------------------
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'user')
    search_fields = ['name', 'user__username']
    raw_id_fields = ('user'),
admin.site.register(Exchange, ExchangeAdmin)
