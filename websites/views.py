from .serializers import websiteSerializer
from .models import website
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from django.conf import settings
import os


class websiteAPIView(views.APIView):
    serializer_class = websiteSerializer

    def post(self, request):
        try:
            # bd = request.body
            # bd["logo"] = bd["logo"].decode('base64')
            logo = request.FILES['logo']
            # logo = base64.b64encode(uploaded_file.read())

            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            whatsapp = request.POST.get('whatsapp')
            instegram_link = request.POST.get('instegram_link')
            facebook_link = request.POST.get('facebook_link')
            about = request.POST.get('about')
            data = {
                "name": name,
                "phone": phone,
                "email": email,
                "whatsapp": whatsapp,
                "instegram_link": instegram_link,
                "facebook_link": facebook_link,
                "logo": logo,
                "about": about
            }
            # data = json.loads(request.body)
            serializer = websiteSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response("Error parse json. Please make sure Content-Type = application/json in headers "+e, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=0):
        try:
            if id == 0:
                data = website.objects.all()
                many = True

            else:
                data = website.objects.get(pk=id)
                many = False
            ser = websiteSerializer(data, many=many)
            return Response(ser.data)
        except Exception as e:
            print(e)
            return Response(f"{e}", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            if not website.objects.filter(pk=id).exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            web = website.objects.get(pk=id)

            data = JSONParser().parse(request)
            print(data)
            fields = ["name", "email", "phone", "whatsapp",
                      "instegram_link", "facebook_link", "about"]
            for field in fields:
                if field not in data:
                    raise Exception(f"{field} not provided in the json")
                else:
                    if not field == "":
                        setattr(web, field, data[field])
            web.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            web = website.objects.filter(pk=id)
            if web.exists():
                web = web.first()
                logo = web.logo
                logo_path = os.path.join(
                    settings.STATIC_ROOT, f'db_images/{logo}')
                print(logo_path)
                os.remove(logo_path)
                web.delete()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


