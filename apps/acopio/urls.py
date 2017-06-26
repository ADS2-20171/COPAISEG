from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (SocioListView, SocioCreateView,
                    SocioUpdateView, SocioDeleteView,
                    ParcelaListView, ParcelaCreateView,
                    ParcelaUpdateView, ParcelaDeleteView)


urlpatterns = [

    # URLS SOCIO
    url(r'^socio/listar/$', login_required(SocioListView.as_view()), name="socio_list"),
    url(r'^socio/crear/$', login_required(SocioCreateView.as_view()), name="socio_add"),
    url(r'^socio/editar/(?P<pk>[^/]+)$',
        login_required(SocioUpdateView.as_view()), name='socio_update'),
    url(r'^socio/eliminar/(?P<pk>[^/]+)$',
        login_required(SocioDeleteView.as_view()), name='socio_delete'),

    # URLS PARCELA
    url(r'^parcela/listar/$', login_required(ParcelaListView.as_view()), name="parcela_list"),
    url(r'^parcela/crear/$', login_required(ParcelaCreateView.as_view()), name="parcela_add"),
    url(r'^parcela/editar/(?P<pk>[^/]+)$',
        login_required(ParcelaUpdateView.as_view()), name='parcela_update'),
    url(r'^parcela/eliminar/(?P<pk>[^/]+)$',
        login_required(ParcelaDeleteView.as_view()), name='parcela_delete'),
]
