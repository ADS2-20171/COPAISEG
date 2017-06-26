from django.conf.urls import url
from .views import RegistroUsuario, Logeo, Inicio
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    url(r'^registrar/$', login_required(RegistroUsuario.as_view()), name="registrarUser"),
    url(r'^accounts/login/$', Logeo.as_view(), name="login"),
    url(r'^salir/$', login_required(views.LogOut), name="logout"),
    url(r'^menu/', login_required(Inicio.as_view()), name="index"),
]
