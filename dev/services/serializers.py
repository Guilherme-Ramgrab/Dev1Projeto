from django.db import models
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from futebol.models.estadio import Estadio

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="services:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email']

class GroupSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="services:group-detail")

    class Meta:
        model = Group
        fields = ['url', 'name']


class EstadioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estadio
        fields = ['id', 'nome', 'cod', 'inauguracao']

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.cod = validated_data.get('cod', instance.cod)
        instance.inauguracao = validated_data.get('inauguracao', instance.inauguracao)
        instance.save()
        return instance

    def create(self, validated_data):
        return Estadio.objects.create(**validated_data)