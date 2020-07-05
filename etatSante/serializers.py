from rest_framework import serializers, fields
from etatSante.models import *


class EtatSanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtatSante
        fields = '__all__'
