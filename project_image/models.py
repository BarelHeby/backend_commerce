from django.db import models
from projects.models import project
from custom_storage import CustomImageStorage
# Create your models here.


class project_image(models.Model):
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    img = models.ImageField(storage=CustomImageStorage())
