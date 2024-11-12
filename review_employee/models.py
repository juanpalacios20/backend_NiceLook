from django.db import models
from client.models import Client
from employee.models import Employee
from appointment.models import Appointment
# Create your models here.

class ReviewEmployee (models.Model):
    autor = models.ForeignKey(Client, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    rating = models.FloatField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.comment