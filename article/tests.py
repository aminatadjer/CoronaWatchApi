import json
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse
from .models import *
from .serializers import *
from rest_framework import status

class ArticleGetTestCase(APITestCase):
    def setUp(self):
        Article.objects.create(titre="test titre article", contenu="test contenu article")
        Article.objects.create(titre="test titre article 2", contenu="test contenu article 2")
        Article.objects.create(titre="test titre article 3", contenu="test contenu article 3")

    def test_get_articles(self):
        response =self.client.get("/api/article/")
        articles= Article.objects.all()
        serializer= ArticleSerializer(articles, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_article(self):
        response =self.client.get("/api/article/1/")
        article =Article.objects.get(pk=1)
        serializer = ArticleSerializer(article, many=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_article(self):
        response = self.client.get("/api/article/30/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ArticlePutTestCase(APITestCase):

    def setUp(self):
        self.article =Article.objects.create(titre="test titre article", contenu="test contenu article")
        self.sup_article={"supprime": True, "vu": True}
        self.valid_article = {"valide": True ,"vu": True,}
        self.valid_article={
                "valide": False,
                "supprime": False,
                "vu": False,
                "titre": "test titre",
                "contenu": "test content article",
                "media": None
        }
        self.invalid_article = {
            "valide": False,
            "supprime": False,
            "vu": False,
            "titre": None,
            "contenu": "test content article",
            "media": None
        }


    #test delete article (logical sup)
    def test_delete_article(self):
        data = json.dumps(self.sup_article)
        response= self.client.put("/api/article/"+str(self.article.pk)+"/ArticleSupprimer/", data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'supprime': True, 'vu': True})
        self.assertEqual(True, True)

    #test valide article
    #test add article without file
    def test_post_valid_article_noFile(self):
        data = json.dumps(self.valid_article)
        response= self.client.post("/api/article/",data=data,content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_invalid_article(self):
        data = json.dumps(self.invalid_article)
        response = self.client.post("/api/article/", data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #test add article with file