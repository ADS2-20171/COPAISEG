from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (PersonaListView, PersonaCreateView,
                    PersonaUpdateView, PersonaDeleteView,
                    UsuarioListView, UsuarioCreateView,
                    UsuarioUpdateView, UsuarioDeleteView)


urlpatterns = [
    # url(r'$', IndexView.as_view(), name="index"),

    # URLS PERSONA
    url(r'^persona/listar/$', login_required(PersonaListView.as_view()), name="persona_list"),
    url(r'^persona/crear/$', login_required(PersonaCreateView.as_view()), name="persona_add"),
    url(r'^persona/editar/(?P<pk>[^/]+)$',
        login_required(PersonaUpdateView.as_view()), name='persona_update'),
    url(r'^persona/eliminar/(?P<pk>[^/]+)$',
        login_required(PersonaDeleteView.as_view()), name='persona_delete'),

    # # URLS USUARIO
    url(r'^usuario/listar/$', login_required(UsuarioListView.as_view()), name="usuario_list"),
    url(r'^usuario/crear/$', login_required(UsuarioCreateView.as_view()), name="usuario_add"),
    url(r'^usuario/editar/(?P<pk>[^/]+)$',
        login_required(UsuarioUpdateView.as_view()), name='usuario_update'),
    url(r'^usuario/eliminar/(?P<pk>[^/]+)$',
        login_required(UsuarioDeleteView.as_view()), name='usuario_delete'),
]
