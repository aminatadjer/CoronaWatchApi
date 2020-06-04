import json
from rest_framework.test import APIRequestFactory, APITestCase,APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import *
from rest_framework import status

class ReportTestCase(APITestCase):

    def setUp(self):
        self.region=Region.objects.create(nom="region test", longitude=0.65, latitude=0.34)
        self.casSignalee= CasSignalee.objects.create(region=Region.objects.filter().first(), commentaire="cas signale test")

    # get all reported case test
    def test_get_reports(self):
        response =self.client.get("/api/casSignaler/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #get one reported case test
    def test_get_report(self):
        response = self.client.get("/api/casSignaler/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #report a case / post test

    #delete a case /put test
    #valide a case /put test
    #delete request test


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

