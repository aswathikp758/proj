from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.IntegerField()
    address=models.CharField(max_length=100)