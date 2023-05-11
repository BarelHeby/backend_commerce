from django.shortcuts import render, get_object_or_404

# Create your views here.
from .serializers import userSerializer
from .models import user
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .form import userForm


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
            data = JSONParser().parse(request)
            serializer = userSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        try:
            if id is None:
                data = user.objects.all()
            else:
                data = user.objects.filter(id=id)
            ser = userSerializer(data, many=True)
            if len(ser.data) == 0:
                return Response(f"id {id} Was Not Found", status=status.HTTP_404_NOT_FOUND)
            return Response(ser.data)
        except Exception as e:
            return Response("Request In wrong format", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            us = get_object_or_404(user, pk=id)
            data = JSONParser().parse(request)
            us.name = data["name"]
            us.email = data["email"]
            us.phone_number = data["phone_number"]
            us.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
