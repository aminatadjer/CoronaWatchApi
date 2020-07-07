from django.shortcuts import render
from map.serializers import *
from map.models import Region
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from notification.models import *
from django.contrib.auth.decorators import permission_required
# Create your views here.
from config import notifArticleTitre, Suj, notifMapTitre, notifRobotTitre, notifVideoUserTitre, notifVidEtRepTitre


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

    @action(detail=False, methods=['get'])
    def getRiskedZones(self, request):
        data = Region.objects.filter(degre=2)
        serializers = RegionSerializer(data, many=True)
        return Response(serializers.data)

    @action(detail=True, methods=['get'])
    def get(self, request, pk=None):
        queryset = Region.objects.get(pk=pk)
        serializer = RegionSerializer(queryset)
        return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def updateRegion(self, request, pk=None):
        try:
            region = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RegionUpdateSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()

            notification = Notification(
                titre=notifMapTitre,
                typeNotif=0,
                description=Suj+" " + region.ArabicName
            )
            notification.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfoRegionViewSet(viewsets.ModelViewSet):
    queryset = HistoriqueRegion.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InfoRegionSerializer

    @action(methods=['put'], detail=True)
    def rejeter(self, request, pk=None):
        try:
            infos = HistoriqueRegion.objects.get(pk=pk)
        except HistoriqueRegion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InfoRegionRejeterSerializer(infos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def valider(self, request, pk=None):

        try:
            infos = HistoriqueRegion.objects.get(pk=pk)
        except HistoriqueRegion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InfoRegionValiderSerializer(infos, data=request.data)
        if serializer.is_valid():

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def get(self, request, pk=None):
        queryset = HistoriqueRegion.objects.get(pk=pk)
        serializer = InfoRegionSerializer(queryset)
        return Response(serializer.data)


class CentreReceptionViewSet(viewsets.ModelViewSet):
    queryset = CentreReception.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CentreReceptionSerializer

    @action(detail=True, methods=['get'])
    def getByRegion(self, request, pk=None):
        queryset = CentreReception.objects.filter(region=pk)
        serializer = CentreReceptionSerializer(queryset, many=True)
        return Response(serializer.data)
