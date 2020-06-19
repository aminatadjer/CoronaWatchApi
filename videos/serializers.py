from rest_framework import serializers, fields
from .models import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoInternaut
        fields = '__all__'


class VideoSerializerValider(serializers.ModelSerializer):
    class Meta:
        model = VideoInternaut
        fields = ['valide', 'vu']


class VideoSerializerSupprimer(serializers.ModelSerializer):
    class Meta:
        model = VideoInternaut
        fields = ['supprime', 'vu']