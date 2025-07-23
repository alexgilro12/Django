import datetime
import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from ProjecteDjangoAlexMarcDavid.models import Platform, Game, User

# Create your views here.
from django.views.generic.base import View


class Prova1(LoginRequiredMixin, View):
    # Definim el mètode HTTP el qual s'ha d'atendre
    def get(self, data):
        return HttpResponse(content='Això és una prova')

class InsertData (View):
    def get(self, data):
        u1 = User.objects.create_user(username='David',password='super3', email='dlopezm@ies-sabadell.cat')
        u2 = User.objects.create_user(username='Alex',password='super3', email='agil@ies-sabadell.cat')
        u3 = User.objects.create_user(username='Marc',password='super3', email='msegala@ies-sabadell.cat')
        u4 = User.objects.create_user(username='Eloi',password='super3', email='evazquez@ies-sabadell.cat')
        p1 = Platform.objects.create(name='Steam',data_de_creacio=datetime.datetime.now())
        p2 = Platform.objects.create(name='PlayStation',data_de_creacio=datetime.datetime.now())
        p3 = Platform.objects.create(name='Xbox', data_de_creacio=datetime.datetime.now())
        p4 = Platform.objects.create(name='Nintendo Switch', data_de_creacio=datetime.datetime.now())
        g1 = Game.objects.create(name='Little Nightmares', price=20, new=True, platform= p1)
        g2 = Game.objects.create(name='Poppy Playtimes', price=15, new=True, platform=p1)
        g3 = Game.objects.create(name='The legend of zelda breath of the wild', price=60, new=False, platform=p4)
        g4 = Game.objects.create(name='Call of Duty Black Ops', price=50, new=False, platform=p2)
        g5 = Game.objects.create(name='Prince of Persia', price=50, new=False, platform=p3)

        p1.users.add(u1, u2, u3)
        p2.users.add(u2, u3, u4)
        p3.users.add(u1, u4)
        p4.users.add(u2, u3)
        p1.save()
        p2.save()
        p3.save()
        p4.save()

        g1.users.add(u1, u2, u3)
        g2.users.add(u2, u3, u4)
        g3.users.add(u1, u4)
        g4.users.add(u2, u3)
        g5.users.add(u3)
        g1.save()
        g2.save()
        g3.save()
        g4.save()
        g5.save()

        return HttpResponse(content='successfull')

#/addVideojoc/{idPlataforma}/{idVideojoc}: Afegeix el videojoc proporcionat a la plataforma proporcionada
class addVid(LoginRequiredMixin, View):
    def get(self,request,idPlat,idVid):
        vid = Game.objects.get(id=idVid)
        plat = Platform.objects.get(id=idPlat)
        vid.platform = plat
        vid.save()
        return HttpResponse(content='Afegit correctament')

class VideojocUsuari(LoginRequiredMixin, View):
    def get(self, request, idG, idU):
        try:
            usuari = User.objects.get(id=idU)
        except User.DoesNotExist:
            raise Http404("Aquest usuari no existeix")

        try:
            joc = Game.objects.get(id=idG)
        except User.DoesNotExist:
            raise Http404("Aquest joc no existeix")

        joc.users.add(usuari)
        joc.save()
        return HttpResponse(content='La afegit correctament')

class EliminarVideojocUsuari(LoginRequiredMixin, View):
    def get(self, request, idG, idU):
        try:
            usuari = User.objects.get(id=idU)
        except User.DoesNotExist:
            raise Http404("Aquest usuari no existeix")

        try:
            joc = Game.objects.get(id=idG)
        except User.DoesNotExist:
            raise Http404("Aquest joc no existeix")

        joc.users.remove(usuari)
        joc.save()
        return HttpResponse(content="S'ha eliminat correctament")

class PlataformasUser(LoginRequiredMixin, View):
    def get(self, request, nom):
        try:
            usuari = User.objects.get(username=nom)
        except User.DoesNotExist:
            raise Http404("Aquest usuari no existeix")

        context = {
            'plataformas': list(Platform.objects.filter(users=usuari))
        }

        return render(request, 'PlataformaUser.html', context=context)


class AddUser(LoginRequiredMixin, View):
    def get(self,request,idPlat,idUser):
        us = User.objects.get(id=idUser)
        plat = Platform.objects.get(id=idPlat)
        plat.users.add(us)  ;
        plat.save()
        return HttpResponse(content='Afegit correctament')


class AddPlataforma(LoginRequiredMixin, View):
    def get(self,request):
        return render(request, 'addPlataforma.html')
    def post(self, request):
        print (request.POST.get("name"))
        name = request.POST.get('name')
        p4 = Platform.objects.create(name=name, data_de_creacio=datetime.datetime.now())
        p4.save()
        return HttpResponse(content='Afegit correctament')


