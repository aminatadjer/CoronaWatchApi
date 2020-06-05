from rest_framework import serializers, fields
from map.models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class CentreReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentreReception
        fields = '__all__'


class RegionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['suspect', 'confirme', 'critique', 'mort',
                  'guerie', 'degre', 'date_validation']


class InfoRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueRegion
        fields = '__all__'


class InfoRegionRejeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueRegion
        fields = fields = ['supprime', 'vu']


class InfoRegionValiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueRegion
        fields = fields = ['valide', 'vu']
