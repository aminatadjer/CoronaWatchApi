import json
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse
from .models import *
from rest_framework import status

class UserCreationTestCase(APITestCase):

    def test_get_users(self):
        response =self.client.get("/api/user/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_creation(self):
        data= {"username":"testcase", "password":"apitestcasepass", "role":"health agent"}
        response = self.client.post('/user/create/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




