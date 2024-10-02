from django.db import models
from establisment.models import Establisment
from payment.models import Payment
from schedule.models import Schedule
from service.models import Service
from client.models import Client

# Create your models here.

class Appointment (models.Model):
    establisment = models.ForeignKey(Establisment, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.DateTimeField()
    estate = models.BooleanField()
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.time
    