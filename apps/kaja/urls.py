from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import MonedaListView, MonedaCreateView, MonedaUpdateView, MonedaDeleteView


urlpatterns = [

    # URLS SOCIO
    url(r'^moneda/listar/$',
        login_required(MonedaListView.as_view()), name="moneda_list"),
    url(r'^moneda/crear/$', login_required(MonedaCreateView.as_view()), name="moneda_add"),
    url(r'^moneda/editar/(?P<pk>[^/]+)$',
        login_required(MonedaUpdateView.as_view()), name='moneda_update'),
    url(r'^moneda/eliminar/(?P<pk>[^/]+)$',
        login_required(MonedaDeleteView.as_view()), name='moneda_delete'),

]
