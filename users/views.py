from django.shortcuts import render, get_object_or_404

# Create your views here.
from .serializers import userSerializer
from .models import user
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .form import userForm
import json


class userAPIView(views.APIView):
    serializer_class = userSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = userSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("Error parse json. Please make sure Content-Type = application/json in headers", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=0):
        try:
            if id == 0:
                data = user.objects.all()
                many = True

            else:
                data = user.objects.get(pk=id)
                many = False
            ser = userSerializer(data, many=many)
            # if len(ser.data) == 0:
            #     return Response(f"id {id} Was Not Found", status=status.HTTP_404_NOT_FOUND)
            return Response(ser.data)
        except Exception as e:
            print(e)
            return Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            us = get_object_or_404(user, pk=id)
            data = JSONParser().parse(request)
            us.name = data["name"] if "name" in data else us.name
            us.email = data["email"] if "email" in data else us.email
            us.phone_number = data["phone_number"] if "phone_number" in data else us.phone_number
            us.website_name = data["website_name"] if "website_name" in data else us.website_name
            us.adminPassword = data["adminPassword"] if "adminPassword" in data else us.adminPassword
            us.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            us = user.objects.filter(pk=id)
            if us.exists():
                us.delete()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
