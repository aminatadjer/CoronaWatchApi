from django.utils import timezone
import json
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse
from .models import *
from .serializers import *
from rest_framework import status

class RegionGetTestCase(APITestCase):
    def setUp(self):
        User.objects.create(username="test", password="mapmap")
        self.region=Region.objects.create(nom="test", suspect=4, confirme=4, critique=2, mort=1, guerie = 2,degre = 1, date_validation =timezone.now())
        self.historique=HistoriqueRegion.objects.create(region=Region.objects.filter().first(),suspect=4, confirme=4, critique=2, mort=1, guerie = 2,degre = 1, agent=User.objects.filter().first() )
        self.centre= CentreReception.objects.create(region=Region.objects.filter().first(), nom='centre test',numero="1", adresse="adresse centre test")


    def test_get_Regions(self):
        response =self.client.get("/api/region/")
        regions= Region.objects.all()
        serializer= RegionSerializer(regions, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_getAll_Regions(self):
        response =self.client.get("/api/region/getAll/")
        regions= Region.objects.all()
        serializer= RegionSerializer(regions, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_Region(self):
        response =self.client.get("/api/region/"+str(self.region.pk)+"/")
        region = Region.objects.get(pk=self.region.pk)
        serializer = RegionSerializer(region, many=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_Regionget(self):
        response =self.client.get("/api/region/"+str(self.region.pk)+"/get/")
        region = Region.objects.get(pk=self.region.pk)
        serializer = RegionSerializer(region, many=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_region(self):
        response = self.client.get("/api/region/30/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_historiques(self):
        response =self.client.get("/api/InfoRegion/")
        historiques= HistoriqueRegion.objects.all()
        serializer= InfoRegionSerializer(historiques, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_get_historique(self):
        response =self.client.get("/api/InfoRegion/"+str(self.historique.pk)+"/")
        historique = HistoriqueRegion.objects.get(pk=self.historique.pk)
        serializer = InfoRegionSerializer(historique, many=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_historique(self):
        response = self.client.get("/api/InfoRegion/30/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_centres(self):
        response =self.client.get("/api/centre/")
        centres= CentreReception.objects.all()
        serializer= CentreReceptionSerializer(centres, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_centre(self):
        response =self.client.get("/api/centre/"+str(self.centre.pk)+"/")
        centre = CentreReception.objects.get(pk=self.centre.pk)
        serializer = CentreReceptionSerializer(centre, many=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_centre(self):
        response = self.client.get("/api/centre/30/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




class RegionPutTestCase(APITestCase):

    def setUp(self):
        User.objects.create(username="test", password="mapmap")
        self.region = Region.objects.create(nom="test", suspect=4, confirme=4, critique=2, mort=1, guerie=2, degre=1,date_validation=timezone.now())
        self.historique = HistoriqueRegion.objects.create(region=Region.objects.filter().first(), suspect=4, confirme=4,critique=2, mort=1, guerie=2, degre=1,agent=User.objects.filter().first())
        self.centre = CentreReception.objects.create(region=Region.objects.filter().first(), nom='centre test',numero="1", adresse="adresse centre test")
        self.rejet_region={"supprime": True, "vu": True}
        self.valid_region = {"valide": True ,"vu": True}
        self.update_region= {
    "suspect": 4,
    "confirme": 3,
    "critique": 3,
    "mort": 3,
    "guerie": 4,
    "degre": 5,
    "date_validation": '2020-06-06T04:41:31.920427Z'}


    def test_rejet_region(self):
        data = json.dumps(self.rejet_region)
        response= self.client.put("/api/InfoRegion/"+str(self.historique.pk)+"/rejeter/", data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'supprime': True, 'vu': True})

    def test_valide_region(self):
        data = json.dumps(self.valid_region)
        response= self.client.put("/api/InfoRegion/"+str(self.historique.pk)+"/valider/", data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'valide': True, 'vu': True})

    def test_update_region(self):
        data = json.dumps(self.update_region)
        response= self.client.put("/api/region/"+str(self.region.pk)+"/updateRegion/", data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.update_region)

    #test valide article
    #test add article without file

class RegionPostTestCase(APITestCase):

    def setUp(self):
        self.user =  User.objects.create(username="test", password="mapmap")
        self.region = Region.objects.create(nom="test", suspect=4, confirme=4, critique=2, mort=1, guerie=2, degre=1,date_validation=timezone.now())
        self.region_playload={
            "nom": "Alger",
            "suspect": 4,
            "confirme": 3,
            "critique": 3,
            "mort": 3,
            "guerie": 4,
            "degre": 5,
            "date_validation": "2020-06-20T01:29:00Z"

        }
        self.centre_playload={
            "nom": "centre test",
            "numero": "1",
            "adresse": "centre adresse test",
            "region": self.region.pk
        }
        self.historique_playload={
            "suspect": 5,
            "confirme": 3,
            "critique": 2,
            "mort": 1,
            "guerie": 1,
            "degre": 1,
            "valide": False,
            "supprime": False,
            "vu": False,
            "region": self.region.pk,
            "agent": self.user.pk
        }

    def test_post_region(self):
        data = json.dumps(self.region_playload)
        response = self.client.post("/api/region/", data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_centre(self):
        data = json.dumps(self.centre_playload)
        response = self.client.post("/api/centre/", data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_historique(self):
        data = json.dumps(self.centre_playload)
        response = self.client.post("/api/centre/", data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)