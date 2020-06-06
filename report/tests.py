import json

from django.utils import timezone
from rest_framework.test import APIRequestFactory, APITestCase,APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import *
from .serializers import *
from rest_framework import status

class ReportGetTestCase(APITestCase):

    def setUp(self):
        self.region = Region.objects.create(nom="test", suspect=4, confirme=4, critique=2, mort=1, guerie=2, degre=1,date_validation=timezone.now())
        self.casSignalee= CasSignalee.objects.create(region=Region.objects.filter().first(), commentaire="cas signale test")

    def test_get_reports(self):
        response =self.client.get("/api/casSignaler/")
        cas = CasSignalee.objects.all()
        serializer = CasSignalerSerializer(cas, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_reports_showList(self):
        response =self.client.get("/api/casSignaler/show_list/")
        cas = CasSignalee.objects.all()
        serializer = CasSignalerSerializer(cas, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_report(self):
        response = self.client.get("/api/casSignaler/"+ str(self.casSignalee.pk)+"/")
        cas = CasSignalee.objects.get(pk=self.casSignalee.pk)
        serializer = CasSignalerSerializer(cas, many=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)



class ReportPutTestCase(APITestCase):

    def setUp(self):
        self.region = Region.objects.create(nom="test", suspect=4, confirme=4, critique=2, mort=1, guerie=2, degre=1,date_validation=timezone.now())
        self.casSignalee= CasSignalee.objects.create(region=Region.objects.filter().first(), commentaire="cas signale test")
        self.sup_cas = {"supprime": True, "vu": True}
        self.valid_cas = {"valide": True, "vu": True}

    def test_sup_cas(self):
        data = json.dumps(self.sup_cas)
        response= self.client.put("/api/casSignaler/"+str(self.casSignalee.pk)+"/CasSignalerSupprimer/", data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'supprime': True, 'vu': True})
"""
    def test_valide_cas(self):
        data = json.dumps(self.valid_cas)
        response= self.client.put("/api/casSignaler/"+str(self.casSignalee.pk)+"/CasSignalerValider/", data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'valide': True, 'vu': True})
"""


class ReportPostTestCase(APITestCase):

    def setUp(self):
        self.region = Region.objects.create(nom="test", suspect=4, confirme=4, critique=2, mort=1, guerie=2, degre=1,date_validation=timezone.now())
        self.cas_playload={
            "valide": False,
            "supprime": False,
            "vu": False,
            "media": None,
            "commentaire": "cas test",
            "region": self.region.pk
        }

    def test_post_cas(self):
        data = json.dumps(self.cas_playload)
        response = self.client.post("/api/casSignaler/", data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
