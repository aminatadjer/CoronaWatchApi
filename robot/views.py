
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from scraper.twitterScrapping import getTweets
from scraper.googleSearchScrapping import ParseFeed
from .serializers import *
from .models import *


class VeilleViewSet(viewsets.ModelViewSet):
    queryset = Veille.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VeilleSerializer
    url = "http://news.google.com/news?q=covid-19&hl=ar-DZ&sort=date&gl=DZ&num=100&output=rss"

    @action(methods=['post', 'get'], detail=False)
    def getData(self, request):
        if(request.method == "GET"):
            feed = ParseFeed(self.url)
            feed.parse()
            getTweets(50)
            data = Veille.objects.all()
            serializers = VeilleSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = VeilleSerializer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()

                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def Supprimer(self, request, pk=None):
        try:
            veille = Veille.objects.get(
                pk=pk)
        except veille.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VeilleSerializerSupprimer(veille, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def Valider(self, request, pk=None):
        try:
            veille = Veille.objects.get(pk=pk)
        except veille.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VeilleSerializerValider(veille, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

