
from rest_framework import viewsets, permissions, status

from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import viewsets, permissions
from .twitterScrapping import getTweets
from .googleSearchScrapping import ParseFeed
from .serializers import *
from .models import *


class VideoYoutubeViewSet(viewsets.ModelViewSet):
    queryset = VideoYoutube.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VideoYoutubeSerializer

    @action(methods=['post', 'get'], detail=False)
    def show_list(self, request):
        if(request.method == "GET"):
            data = VideoYoutube.objects.all()
            serializers = VideoYoutubeSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = VideoYoutubeSerializer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()

                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def VideoSupprimer(self, request, pk=None):
        try:
            video = VideoYoutube.objects.get(
                pk=pk)
        except VideoYoutube.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VideoYoutubeSerializerSupprimer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def VideoValider(self, request, pk=None):
        try:
            video = VideoYoutube.objects.get(pk=pk)
        except VideoYoutube.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VideoYoutubeSerializerValider(video, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleSearchViewSet(viewsets.ModelViewSet):
    queryset = GoogleSearchResult.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GoogleSearchSerializer
    url = "http://news.google.com/news?q=covid-19&hl=ar-DZ&sort=date&gl=DZ&num=100&output=rss"
    @action(methods=['post', 'get'], detail=False)
    def getData(self, request):
        if(request.method == "GET"):
            feed = ParseFeed(self.url)
            feed.parse()
            data = GoogleSearchResult.objects.all()
            serializers = GoogleSearchSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = GoogleSearchSerializer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def googleSupprimer(self, request, pk=None):
        try:
            google = GoogleSearchResult.objects.get(pk=pk)
        except GoogleSearchResult.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GoogleSearchSerializerSupprimer(google, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def googleValider(self, request, pk=None):
        try:
            google = GoogleSearchResult.objects.get(pk=pk)
        except google.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GoogleSearchSerializerValider(google, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TweetsViewSet(viewsets.ModelViewSet):
    queryset = Tweets.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TweetSerializer

    @action(methods=['post', 'get'], detail=False)
    def getData(self, request):
        if(request.method == "GET"):
            getTweets(50)
            data = Tweets.objects.all()
            serializers = TweetSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = TweetSerializer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()

                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def TweetSupprimer(self, request, pk=None):
        try:
            tweet = Tweets.objects.get(pk=pk)
        except Tweets.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TweetSerializerSupprimer(tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def TweetValider(self, request, pk=None):
        try:
            tweet = Tweets.objects.get(pk=pk)
        except Tweets.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TweetSerializerValider(tweet, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
