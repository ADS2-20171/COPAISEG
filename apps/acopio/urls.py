from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import SocioListView, SocioCreateView
#                     , SocioCreateView,SocioUpdateView, SocioDeleteView)


urlpatterns = [

    # URLS SOCIO
    url(r'^socio/listar/$', login_required(SocioListView.as_view()), name="socio_list"),
    url(r'^socio/crear/$', login_required(SocioCreateView.as_view()), name="socio_add"),
    # url(r'^socio/editar/(?P<pk>[^/]+)$',
    #     login_required(SocioUpdateView.as_view()), name='socio_update'),
    # url(r'^socio/eliminar/(?P<pk>[^/]+)$',
    #     login_required(SocioDeleteView.as_view()), name='socio_delete'),
]
