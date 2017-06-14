from django.conf.urls import url
from .views import RegistroUsuario, Logeo, Inicio
from . import views


urlpatterns = [
    url(r'^registrar/$', RegistroUsuario.as_view(), name="registrarUser"),
    url(r'^login/$', Logeo.as_view(), name="login"),
    url(r'^salir/$', views.LogOut, name="logout"),
    url(r'^menu/', Inicio.as_view(), name="index"),
]
