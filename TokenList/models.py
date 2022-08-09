from operator import mod
from select import select
from statistics import mode
from unicodedata import decimal
from django.db import models

# Create your models here.


class TokenModel(models.Model):
    channel_id = models.CharField(max_length=5,null=True,default="")
    name = models.CharField(max_length=50, null=True, )
    selected = models.BooleanField(null=True)
    symbol = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=250, null=True)
    decimals = models.IntegerField(null=True)
    logoURI = models.CharField(max_length=250, null=True)
    chainId = models.IntegerField(null=True)
    pairs = models.CharField(max_length=250, null=True)
    type = models.CharField(max_length=30,null=True)
    asset = models.CharField(max_length=50, null=True)


    def __str__(self) -> str:
        return self.symbol
