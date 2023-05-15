from django.db import models
from custom_storage import CustomImageStorage
# Create your models here.


class website(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(storage=CustomImageStorage())
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=15)
    instegram_link = models.CharField(max_length=150)
    facebook_link = models.CharField(max_length=150)
    facebook_link = models.CharField(max_length=150)
    about = models.TextField(default="", null=False)
