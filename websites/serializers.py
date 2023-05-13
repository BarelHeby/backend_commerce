from .models import website
from rest_framework import serializers


class websiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = website
        fields = '__all__'
