from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    designer_name = models.CharField(max_length=20,default='sMr.Dilip Gajjar')
    service_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}'s booking for {self.service_name} Interiores Services"
    
# Create your models here.
