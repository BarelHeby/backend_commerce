from django.db import models
from websites.models import website
# Create your models here.


class phase(models.Model):

    website = models.OneToOneField(website, on_delete=models.CASCADE)
    phase_1 = models.CharField(max_length=100)
    phase_1_header = models.CharField(max_length=100)
    phase_2 = models.CharField(max_length=100)
    phase_2_header = models.CharField(max_length=100)
    phase_3 = models.CharField(max_length=100)
    phase_3_header = models.CharField(max_length=100)
    phase_4 = models.CharField(max_length=100)
    phase_4_header = models.CharField(max_length=100)
