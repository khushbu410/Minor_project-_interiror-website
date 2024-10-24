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


# new Vastu AI feature
class Room(models.Model):
    name = models.CharField(max_length=100)

class Direction(models.Model):
    name = models.CharField(max_length=50)

class VastuUpload(models.Model):
    house_plan = models.ImageField(upload_to='house_plans/')
    direction = models.CharField(max_length=20, choices=[
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East'),
        ('W', 'West')
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)

# class VastuRule(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
#     rule_description = models.TextField()

# class UserVastuCheck(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)  

