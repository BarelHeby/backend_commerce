from .models import project_image
from rest_framework import serializers


class projectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = project_image
        fields = '__all__'
