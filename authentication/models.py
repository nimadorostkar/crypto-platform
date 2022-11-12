from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.custom_usermanager import UserManager
from django.utils.html import format_html



#-------------------------------------------------------------------------------
class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=256, unique=True)
    photo = models.ImageField(upload_to='user/photo', default='user/photo/default.png', null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    confirmed = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return str(self.username)

    def img(self):
        return format_html("<img style='width:30px;border-radius:50%;' src='{}'>".format(self.photo.url))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
