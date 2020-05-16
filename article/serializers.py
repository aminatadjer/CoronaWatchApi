from rest_framework import serializers, fields
from article.models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializerValider(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['valide', 'vu']


class ArticleSerializerSupprimer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['supprime', 'vu']
