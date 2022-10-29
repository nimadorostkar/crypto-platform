from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html

#-------------------------------------------------------------------------------
class User(AbstractUser):
    photo = models.ImageField(upload_to='user/photo', default='user/photo/default.png', null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.username)

    def img(self):
        return format_html("<img width=30 src='{}'>".format(self.photo.url))
