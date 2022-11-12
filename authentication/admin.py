from django.contrib import admin
from .models import User


#-------------------------------------------------------------------------------
class UserAdmin(admin.ModelAdmin):
    list_display = ('img', 'email', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ['email', 'firs_name', 'last_name']
admin.site.register(User, UserAdmin)
