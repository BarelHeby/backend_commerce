from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import projectSerializer
from .models import project
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class projectAPIView(views.APIView):
    serializer_class = projectSerializer

    def check_vaildality(self, request):
        params = request.query_params
        if "user_id" in params:
            return params
        return None

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = projectSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"reasone": "Request In Wrong Format", "Request": request}, status=400)

    def get(self, request, id=None):
        try:
            params = self.check_vaildality(request)
            if not params:
                return Response("user id is not mention in parameters", status=status.HTTP_400_BAD_REQUEST)
            data = project.objects.filter(user=params["user_id"])
            if id:
                data = data.filter(pk=id)
            if "is_in_use" in params:
                data = data.filter(is_in_use=params["is_in_use"])
            serializer = projectSerializer(data, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response("Request In wrong format", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            if id is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            project.objects.filter(id=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            if not id:
                raise Exception("Please specify the id of the project")

            params = self.check_vaildality(request)
            if not params:
                return Response("user id is not mention in parameters", status=status.HTTP_400_BAD_REQUEST)
            proj = project.objects.get(pk=id, user=params["user_id"])
            data = JSONParser().parse(request)
            if "title" in data:
                proj.title = data["title"]
            if "description" in data:
                proj.description = data["description"]
            if "is_in_use" in data:
                proj.is_in_use = data["is_in_use"]
            proj.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
