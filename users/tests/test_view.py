from django.test import TestCase, Client
from django.urls import reverse
from users.models import user
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.new_user = user.objects.create(
            name="barel",
            phone_number="0543510535",
            email="barelheby03@gmail.com",
            website_name="barel website",
            adminPassword="123456"
        )

    def test_users_GET(self):
        response_users = self.client.get(reverse('users'))
        self.assertEquals(response_users.status_code, 200)

    def test_users_id_GET(self):
        resp = self.client.get(reverse('users_id', args=[self.new_user.id]))
        self.assertEquals(resp.status_code, 200)
        js = resp.json()
        self.assertEquals(js["name"], self.new_user.name)
        self.assertEquals(js["phone_number"], self.new_user.phone_number)
        self.assertEquals(js["email"], self.new_user.email)
        self.assertEquals(js["website_name"], self.new_user.website_name)
        self.assertEquals(js["adminPassword"], self.new_user.adminPassword)

    def test_users_POST(self):
        new_user = {
            "name": "barel_2",
            "phone_number": "0543510535",
            "email": "barelheby03@gmail.com",
            "website_name": "barel website",
            "adminPassword": "123456"
        }
        resp = self.client.post(reverse('users'), new_user, "application/json")

        self.assertEquals(resp.status_code, 201)

        self.assertEquals(user.objects.get(
            pk=resp.json()["id"]).name, new_user["name"])
        self.assertEquals(user.objects.get(
            pk=resp.json()["id"]).phone_number, new_user["phone_number"])
        self.assertEquals(user.objects.get(
            pk=resp.json()["id"]).email, new_user["email"])
        self.assertEquals(user.objects.get(
            pk=resp.json()["id"]).website_name, new_user["website_name"])
        self.assertEquals(user.objects.get(
            pk=resp.json()["id"]).adminPassword, new_user["adminPassword"])

    def test_users_PUT_update_exist(self):
        new_user = user.objects.create(
            name="update_test",
            phone_number="051021654",
            email="email_update_test",
            website_name="web_update_test",
            adminPassword="admin_update_test"
        )
        update_user = {
            "name": "barel_2",
            "phone_number": "0543510535",
            "email": "barelheby03@gmail.com",
            "website_name": "barel website",
            "adminPassword": "123456"
        }
        resp = self.client.put(
            reverse('users_id', args=[new_user.id]), update_user, "application/json")
        self.assertEquals(resp.status_code, 202)

        self.assertEquals(user.objects.get(
            pk=new_user.id).name, update_user["name"])
        self.assertEquals(user.objects.get(
            pk=new_user.id).phone_number, update_user["phone_number"])
        self.assertEquals(user.objects.get(
            pk=new_user.id).email, update_user["email"])
        self.assertEquals(user.objects.get(
            pk=new_user.id).website_name, update_user["website_name"])
        self.assertEquals(user.objects.get(
            pk=new_user.id).adminPassword, update_user["adminPassword"])

    def test_users_PUT_update_Non_exist(self):
        update_user = {
            "name": "barel_2",
            "phone_number": "0543510535",
            "email": "barelheby03@gmail.com",
            "website_name": "barel website",
            "adminPassword": "123456"
        }
        resp = self.client.put(
            reverse('users_id', args=[5456]), update_user, "application/json")
        self.assertEquals(resp.status_code, 404)

    def test_users_DELETE_existing(self):
        new_user = user.objects.create(
            name="update_test",
            phone_number="051021654",
            email="email_update_test",
            website_name="web_update_test",
            adminPassword="admin_update_test"
        )

        resp = self.client.delete(
            reverse('users_id', args=[new_user.id]))
        self.assertEquals(resp.status_code, 200)

    def test_users_DELETE_Non_existing(self):

        resp = self.client.delete(
            reverse('users_id', args=[100015456]))
        self.assertEquals(resp.status_code, 404)
