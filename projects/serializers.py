from .models import project
from rest_framework import serializers


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'
