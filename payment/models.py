from django.db import models
from client.models import Client
from establisment.models import Establisment
# Create your models here.

class Payment (models.Model):
    state = models.BooleanField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    establisment = models.ForeignKey(Establisment, on_delete=models.CASCADE)
    total = models.FloatField()
    discount = models.FloatField(null = True)
    date = models.DateField()
    method = models.CharField(max_length=50)

    
    def __str__ (self):
        return self.client.user.username 
    