from django.db import models
from authentication.models import User


#-------------------------------------------------------------------------------
class Exchange(models.Model):
    #exchange =
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    api_key = models.CharField(max_length=256, null=True, blank=True)
    api_secret = models.CharField(max_length=256, null=True, blank=True)
    api_passphrase = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    CHOICES = ( ('not-active','not-active'),('active','active'))
    status = models.CharField(max_length=30,choices=CHOICES, default='not-active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
