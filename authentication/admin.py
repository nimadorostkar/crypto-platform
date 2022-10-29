from django.contrib import admin
from .models import User


#-------------------------------------------------------------------------------
class UserAdmin(admin.ModelAdmin):
    list_display = ('img', 'username', 'email', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ['email', 'firs_name', 'last_name', 'username']
admin.site.register(User, UserAdmin)
