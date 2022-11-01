from django.db import models
from authentication.models import User
from django.utils.html import format_html


#-------------------------------------------------------------------------------
class TradeType(models.Model):
    name=models.CharField(unique=True, max_length=256)

    def __str__(self):
        return str(self.name)


#-------------------------------------------------------------------------------
class SourceExchange(models.Model):
    CHOICES=(('yes','yes'),('no','no'),('soon','soon'))
    name=models.CharField(unique=True, max_length=256)
    order_types= models.ManyToManyField(TradeType, blank=True)
    smart_trade=models.CharField(max_length=5,choices=CHOICES,default='soon')
    dca_bot=models.CharField(max_length=5,choices=CHOICES,default='soon')
    grid_bot=models.CharField(max_length=5,choices=CHOICES,default='soon')
    options_bot=models.CharField(max_length=5,choices=CHOICES,default='soon')
    logo=models.ImageField(upload_to='exchange/logo', default='exchange/logo/default.png')
    cover=models.ImageField(upload_to='exchange/cover', default='exchange/cover/default.png')

    def __str__(self):
        return str(self.name)

    def logo_img(self):
        return format_html("<img style='width:30px;border-radius:50%;' src='{}'>".format(self.logo.url))




#-------------------------------------------------------------------------------
class Exchange(models.Model):
    exchange =  models.ForeignKey(SourceExchange, on_delete=models.CASCADE)
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
