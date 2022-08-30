from django.contrib import admin
from django.urls import path
from jobconvo.views import lista_vagas
from jobconvo.views import home, create, store, painel, dologin, dashboard, logouts, changePassword, createVaga, lista_vagas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('create/',create),
    path('store/',store),
    path('painel/',painel),
    path('dologin/',dologin),
    path('dashboard/',dashboard),
    path('logouts/',logouts),
    path('password/',changePassword),
    path('createVaga/',createVaga),
    path('lista_vagas/',lista_vagas)
]
