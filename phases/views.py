from django.shortcuts import render

# Create your views here.
from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import phaseSerializer
from .models import phase
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
import json


class phaseAPIView(views.APIView):
    serializer_class = phaseSerializer

    def check_vaildality(self, request):
        params = request.query_params
        if "website_id" in params:
            return params
        return None

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = phaseSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response("check if phases already exists for this website id", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        try:
            params = self.check_vaildality(request)
            if not params:
                return Response("website id is not mention in parameters", status=status.HTTP_400_BAD_REQUEST)
            data = phase.objects.filter(website=params["website_id"])
            serializer = phaseSerializer(data, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response("Request In wrong format", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            if id is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            phase.objects.filter(website=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            if not id:
                raise Exception("Please specify the id of the website")

            phas = phase.objects.get(website=id)
            data = json.loads(request.body.decode('utf-8'))
            try:
                phase_1 = data["phase_1"]
                phas.phase_1 = phase_1
            except Exception as e:
                pass
            try:
                phase_2 = data["phase_2"]
                phas.phase_2 = phase_2
            except:
                pass
            try:
                phase_3 = data["phase_3"]
                phas.phase_3 = phase_3
            except:
                pass
            try:
                phase_4 = data["phase_4"]
                phas.phase_4 = phase_4
            except:
                pass
            phas.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
