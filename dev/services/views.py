from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from django.contrib.auth.models import Group, User
from services.serializers import *
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from futebol.models.estadio import Estadio
from rest_framework.views import APIView



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET'])
def saudacao(request):
    return Response({"saudacao": "Ola Mundo"})

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'groups': reverse('services:group-list', request=request, format=format),
        'users': reverse('services:user-list', request=request, format=format),
        'saudacao': reverse('services:saudacao', request=request, format=format),
        'estadios': reverse('services:estadios', request=request, format=format)
    })

class EstadioService(APIView):
    queryset = Estadio.objects.all()
    serializer_class = EstadioSerializer

    def get_object(self, pk):
        try:
            return Estadio.objects.get(pk=pk)
        except Estadio.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # def get(self, request, pk, format=None):
    #     estadio = self.get_object(pk)
    #     context = {
    #         'request': request,
    #         'format': format
    #     }
    #     serializer = EstadioSerializer(estadio, context=context)
    #     return Response(serializer.data)

    def get(self, request, format=None):
        estadios = Estadio.objects.all()
        context = {
            'request': request,
            'format': format
         }
        serializer = EstadioSerializer(estadios, many=True, context=context)
        return Response(serializer.data)

    def put(selfself, request, pk, format=None):
        estadio = self.get.object(pk)
        dados = request.data
        context = {
            'request': request,
            'format': format
        }

        serializer = EstadioSerializer(estadio, data=dados, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        estadio = self.get_object(pk)
        estadio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        dados = request.data
        context = {
            'request': request,
            'format': format
        }
        serializer = EstadioSerializer(data=dados, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
