"""ProjecteDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import ProjecteDjangoAlexMarcDavid.views
from ProjecteDjangoAlexMarcDavid.views import Prova1, InsertData, PlataformasUser, EliminarVideojocUsuari, VideojocUsuari, AddPlataforma
from users.views import LoginView, LogoutView
from ProjecteDjangoAlexMarcDavid.api.views import platRndm, platNom, PlataformaRandomNou

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Prova1.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('insertData', InsertData.as_view()),
    path('plataformaRandom', platRndm.as_view()),
    path('PlataformaDe/<nom>', platNom.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('PlataformesDe/<nom>', PlataformasUser.as_view(), name='PlataformaUser'),
    path('removeVideojoc/<idG>/<idU>', EliminarVideojocUsuari.as_view()),
    path('videojoc/<idG>/<idU>', VideojocUsuari.as_view()),
    path('plataformaRandomNou', PlataformaRandomNou.as_view()),
    path('addPlataforma', AddPlataforma.as_view(), name='addPlataforma')

]


