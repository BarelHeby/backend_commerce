from django.shortcuts import render

# Create your views here.
from .serializers import projectImageSerializer
from .models import project_image
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
import json
import base64
from django.conf import settings
import os


class projectImagesAPIView(views.APIView):
    serializer_class = projectImageSerializer

    def post(self, request, id):
        try:
            img = request.FILES['img']
            data = {
                "project": id,
                "img": img
            }

            serializer = projectImageSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("Error parse json. Please make sure Content-Type = application/json in headers "+e, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        try:
            data = project_image.objects.filter(project=id)
            ser = projectImageSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            print(e)
            return Response(f"{e}", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            proj = project_image.objects.filter(pk=id)
            if proj.exists():
                proj = proj.first()
                img = proj.img
                img_path = os.path.join(
                    settings.STATIC_ROOT, f'db_images/{img}')
                os.remove(img_path)
                proj.delete()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
