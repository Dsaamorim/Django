from django.contrib import admin
from django.urls import path
from jobconvo.views import lista_vagas
from jobconvo.views import home, create, store, painel, dologin, dashboard, logouts, changePassword, createVaga, createVagaSalarial, createNivelEscolar, lista_vagas, detalhe_vaga
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home, name = 'home'),
    path('create/',create, name = 'create'),
    path('store/',store, name = 'store'),
    path('painel/',painel, name = 'painel'),
    path('dologin/',dologin, name = 'dologin'),
    path('dashboard/',dashboard, name = 'dashboard'),
    path('logouts/',logouts, name = 'logouts'),
    path('password/',changePassword, name = 'password'),
    path('createVaga/',createVaga, name = 'createVaga'),
    path('lista_vagas/',lista_vagas, name = 'lista_vagas'),
    path('createVagaSalarial/',createVagaSalarial, name = 'createVagaSalarial'),
    path('createNivelEscolar/',createNivelEscolar, name = 'createNivelEscolar'),
    path('detalhe_vaga/<int:pk>/',detalhe_vaga, name = 'detalhe_vaga'),
]
