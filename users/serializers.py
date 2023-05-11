from . import models
from rest_framework import serializers
from rest_framework.fields import IntegerField, CharField, DateTimeField, BooleanField


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = ["id", "name", "phone_number",
                  "email", "website_name", "adminPassword"]
