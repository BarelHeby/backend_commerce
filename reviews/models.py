from django.db import models
from websites.models import website
# Create your models here.


class review(models.Model):
    website_id = models.ForeignKey(website, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()
    insert_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + self.review + str(self.rating)
