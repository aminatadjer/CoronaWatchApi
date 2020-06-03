import json
from rest_framework.test import APIRequestFactory, APITestCase,APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import *
from rest_framework import status

class ReportTestCase(APITestCase):

    def setUp(self):
        self.region=Region.objects.create(nom="region test", confirme=4, mort=3, guerie=5, critique=2, suspect=3)
        self.casSignalee= CasSignalee.objects.create(region=Region.objects.filter().first(), commentaire="cas signale test")
        print("regioon", Region.objects.filter().first())


    def test_get_reports(self):
        response =self.client.get("/api/casSignaler/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_report(self):
        response = self.client.get("/api/casSignaler/1/")
        print('cas signale test', response.data)
        print('\n cas signale test status', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""
    def test_get_report(self):

        data={
    "valide": "false",
    "supprime": "false",
    "vu": "false",
    "date": "2020-06-03T17:13:00.306432Z",
    "commentaire": "kkkk",
    "region": 1
}
        response = self.client.post("/api/casSignaler/", data,  format='multipart')
        print("statuus" ,response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
"""

