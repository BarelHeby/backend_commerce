from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    website_name = models.CharField(max_length=100, default=None)
    adminPassword = models.CharField(max_length=50, default=None)
