from rest_framework import serializers, fields
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'




class CommentSerializerSupprimer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['supprime']