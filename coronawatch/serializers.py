from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer





class UserCreateSerializer(UserCreateSerializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance





