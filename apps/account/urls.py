from django.conf.urls import url
from .views import (PersonaListView, PersonaCreateView,
                    PersonaUpdateView, PersonaDeleteView,
                    UsuarioListView, UsuarioCreateView,
                    UsuarioUpdateView, UsuarioDeleteView)


urlpatterns = [
    # URLS PERSONA
    url(r'^persona/listar/$', PersonaListView.as_view(), name="persona_list"),
    url(r'^persona/crear/$', PersonaCreateView.as_view(), name="persona_add"),
    url(r'^persona/editar/(?P<pk>[^/]+)$',
        PersonaUpdateView.as_view(), name='persona_update'),
    url(r'^persona/eliminar/(?P<pk>[^/]+)$',
        PersonaDeleteView.as_view(), name='persona_delete'),

    # # URLS USUARIO
    url(r'^usuario/listar/$', UsuarioListView.as_view(), name="usuario_list"),
    url(r'^usuario/crear/$', UsuarioCreateView.as_view(), name="usuario_add"),
    url(r'^usuario/editar/(?P<pk>[^/]+)$',
        UsuarioUpdateView.as_view(), name='usuario_update'),
    url(r'^usuario/eliminar/(?P<pk>[^/]+)$',
        UsuarioDeleteView.as_view(), name='usuario_delete'),
]
