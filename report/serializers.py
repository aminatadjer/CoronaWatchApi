from rest_framework import serializers, fields
from report.models import *


class CasSignalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasSignalee
        fields = '__all__'


class CasSignalerSerializerValider(serializers.ModelSerializer):
    class Meta:
        model = CasSignalee
        fields = ['valide', 'vu']


class CasSignalerSerializerSupprimer(serializers.ModelSerializer):
    class Meta:
        model = CasSignalee
        fields = ['supprime', 'vu']
