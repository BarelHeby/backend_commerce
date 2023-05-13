from .models import phase
from rest_framework import serializers


class phaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = phase
        fields = '__all__'
