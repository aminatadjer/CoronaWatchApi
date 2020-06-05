import json
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse
from .models import *
from rest_framework import status

class ArticleTestCase(APITestCase):

    def setUp(self):
        Article.objects.create(titre="test titre article", contenu= "test contenu article")
        Article.objects.create(titre="test titre article 2", contenu="test contenu article 2")
        Article.objects.create(titre="test titre article 3", contenu="test contenu article 3")

    def test_get_articles(self):
        response =self.client.get("/api/article/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_article(self):
        response =self.client.get("/api/article/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)