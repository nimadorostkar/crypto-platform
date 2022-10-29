from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html






class User(AbstractUser):
    first_name = None
    last_name = None
    is_teacher = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    bio = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.username)
