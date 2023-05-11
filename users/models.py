from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
