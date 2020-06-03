from django.shortcuts import render
from map.serializers import *
from map.models import Region
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegionSerializer

    @action(detail=False, methods=['get'])
    def getAll(self, request):
        queryset = Region.objects.all()
        serializer = RegionSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get(self, request, pk=None):
        queryset = Region.objects.get(pk=pk)
        serializer = RegionSerializer(queryset)
        return Response(serializer.data)


class InfoRegionViewSet(viewsets.ModelViewSet):
    queryset = InfoRegion.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InfoRegionSerializer
