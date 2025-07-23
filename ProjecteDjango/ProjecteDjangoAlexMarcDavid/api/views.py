import json

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ProjecteDjangoAlexMarcDavid.models import Platform, User, Game
import random;

from ProjecteDjangoAlexMarcDavid.api.serializers import PlatformSerializer,GameSerializer,UserSerializer


class platRndm(LoginRequiredMixin, APIView):
    def get(self,request):
        items = list(Platform.objects.all())
        platform = PlatformSerializer(random.choice(items))
        return Response(data=platform.data, status=status.HTTP_200_OK)

class platNom(LoginRequiredMixin, APIView):
    def get(self,request,nom):
        user = get_object_or_404(User, username=nom)
        items = list(Platform.objects.filter(users=user))
        if(items.__len__()>0):
            platform = PlatformSerializer(random.choice(items))
            return Response(data=platform.data, status=status.HTTP_200_OK)
        else:
            return Response(data='No té plataformes', status=status.HTTP_204_NO_CONTENT)

class PlataformaRandomNou(APIView):
    def get(self, request):
        # Exemple de com podem usar operadors com contains o like
        plataformas = list(Platform.objects.all())

        listaPlataformas = []

        for plataforma in plataformas:
            videojocs = list(Game.objects.filter(platform=plataforma))
            for videojoc in videojocs:
                if videojoc.new == True:
                    listaPlataformas.append(plataforma)
                    break

        platform = PlatformSerializer(random.choice(listaPlataformas))
        return Response(data=platform.data, status=status.HTTP_200_OK)