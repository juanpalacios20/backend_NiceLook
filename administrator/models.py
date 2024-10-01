from django.db import models
from django.contrib.auth.models import User
from establisment.models import Establisment

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True)
    establisment = models.ForeignKey(Establisment, on_delete=models.CASCADE, null=True)
    
    def __str__ (self):
        return self.user.username