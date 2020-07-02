from rest_framework import serializers, fields
from .models import *


class VeilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veille
        fields = '__all__'


class VeilleSerializerValider(serializers.ModelSerializer):
    class Meta:
        model = Veille
        fields = ['valide']


class VeilleSerializerSupprimer(serializers.ModelSerializer):
    class Meta:
        model = Veille
        fields = ['supprime']

