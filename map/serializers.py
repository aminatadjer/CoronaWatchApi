from rest_framework import serializers, fields
from map.models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class InfoRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoRegion
        fields = '__all__'
