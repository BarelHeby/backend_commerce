from rest_framework import views, status
from .models import website
from rest_framework.response import Response
import os


class websiteLogoAPIView(views.APIView):
    def put(self, request, id):
        try:
            img = request.FILES['img']
            web = website.objects.get(pk=id)
            os.remove(web.logo.path)
            web.logo = img
            web.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
