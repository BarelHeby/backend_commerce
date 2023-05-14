from django.db import models
from websites.models import website
# Create your models here.


class project(models.Model):
    website = models.ForeignKey(
        website, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    insert_date = models.DateTimeField()
    is_in_use = models.BooleanField(default=False)
