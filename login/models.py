from django.db import models
from django.utils import timezone
# Create your models here.
class register(models.Model):
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    Email=models.CharField(max_length=50)
    Phone=models.IntegerField(default=0)
    Date=models.DateTimeField(default=timezone.now)
    Healthy=models.IntegerField(default=0)
    Total=models.IntegerField(default=0)