from django.db import models
from users.models import user
# Create your models here.


class project(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    insert_date = models.DateTimeField()
    is_in_use = models.BooleanField(default=False)
