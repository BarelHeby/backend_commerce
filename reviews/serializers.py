from .models import review
from rest_framework import serializers


class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'
