from rest_framework import serializers, fields
from .models import *

class GoogleSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleSearchResult
        fields = '__all__'


class GoogleSearchSerializerValider(serializers.ModelSerializer):
    class Meta:
        model = GoogleSearchResult
        fields = ['valide']


class GoogleSearchSerializerSupprimer(serializers.ModelSerializer):
    class Meta:
        model = GoogleSearchResult
        fields = ['supprime']


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = '__all__'


class TweetSerializerValider(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['valide']


class TweetSerializerSupprimer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['supprime']


class VideoYoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoYoutube
        fields = '__all__'


class VideoYoutubeSerializerValider(serializers.ModelSerializer):
    class Meta:
        model = VideoYoutube
        fields = ['valide']


class VideoYoutubeSerializerSupprimer(serializers.ModelSerializer):
    class Meta:
        model = VideoYoutube
        fields = ['supprime']


