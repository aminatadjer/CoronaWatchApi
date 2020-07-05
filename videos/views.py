
from rest_framework import viewsets, permissions, status

from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from sendMail.views import send
from notification.models import *
from rest_framework import viewsets, permissions


from .serializers import *
from .models import *
from config import notifArticleTitre, Yours, Suj, notifMapTitre, notifRobotTitre, notifVideoUserTitre, notifVidEtRepTitre


class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoInternaut.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VideoSerializer

    @action(methods=['post', 'get'], detail=False)
    def show_list(self, request):
        if(request.method == "GET"):
            data = VideoInternaut.objects.all()
            serializers = VideoSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = VideoSerializer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def VideoSupprimer(self, request, pk=None):
        try:
            video = VideoInternaut.objects.get(pk=pk)
        except VideoInternaut.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VideoSerializerSupprimer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def VideoValider(self, request, pk=None):
        try:
            video = VideoInternaut.objects.get(pk=pk)
        except VideoInternaut.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VideoSerializerValider(video, data=request.data)

        if serializer.is_valid():
            serializer.save()
            notification = Notification(
                titre=notifVideoUserTitre,
                typeNotif=0,
                description=Suj+" "+video.commentaire
            )
            notification.save()
            notification = Notification(
                titre=notifVidEtRepTitre,
                typeNotif=1,
                description=Yours+" "+video.commentaire
            )
            notification.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def getValidate(self, request):
        if (request.method == "GET"):
            data = VideoInternaut.objects.filter(valide=True)
            serializers = VideoSerializer(data, many=True)
            return Response(serializers.data)
