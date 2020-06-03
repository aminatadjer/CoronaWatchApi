from django.shortcuts import render
from article.models import Article
from rest_framework import viewsets, permissions, status
from article.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from django.core.files import File

from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from datetime import datetime
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ArticleSerializer

    @action(methods=['post', 'get', 'put'], detail=False)
    def ArticleAdd(self, request):

        if(request.method == "GET"):
            data = Article.objects.all()
            serializers = ArticleSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = ArticleSerializer(data=request.data)
            print(str(request.data))
            if(serializers.is_valid()):
                media = ""
                media = str(request.data['media'])
                content = request.data['contenu']
                title = request.data['titre']
                displayMedia = ""
                if media.endswith("mp4"):
                    displayMedia = """<video width="80%" height="80%" controls><source src ="../""" + \
                        media + """ \"  type=\"video/mp4\"\></video>"""

                else:
                    displayMedia = """<img width="80%" height="80%" src="../""" + \
                        media+""" \" ></img>"""

                aaa = render_to_string(
                    'index.html', {'media': displayMedia, 'Title': title, 'content': content})
                print(aaa)
                instance = serializers.save()
                instance_id = instance.id
                nameF = 'media/articles/article' + str(instance_id)+'.html'
                mydata = request.data
                mydata['url'] = nameF
                serializers = ArticleSerializer(data=mydata)
                if(serializers.is_valid()):
                    serializers.save()
                f = open(nameF, 'w')
                f.write(aaa)
                f.close()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def ArticleSupprimer(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializerSupprimer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def ArticleValider(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializerValider(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def ArticleAll(self, request):
        if(request.method == "GET"):
            data = Article.objects.all()
            serializers = ArticleSerializerURL(data, many=True)
            return Response(serializers.data)
