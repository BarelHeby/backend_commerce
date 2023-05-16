from django.shortcuts import render
from .models import review
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import reviewSerializer


class reviewAPIView(views.APIView):
    def get(self, request, id):
        try:
            data = review.objects.filter(website_id=id).order_by(
                '-insert_date', '-rating')[:8]
            ser = reviewSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            print(e)
            return Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = reviewSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)
