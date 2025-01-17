from django.db import models
from employee.models import Employee
from establisment.models import Establisment
from service.models import Service
from client.models import Client

# Create your models here.

class Appointment (models.Model):
    establisment = models.ForeignKey(Establisment, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.DateTimeField()
    estate = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    method = models.CharField(max_length=50)
    event_id = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.client.user.username
    
    @property
    def total_price(self):
        total = 0
        for service in self.services.all():
            total += service.price
        return total
    
    @property
    def commision(self):
        commision = 0
        for service in self.services.all():
            commision += (service.price * service.commission)
        return commision
