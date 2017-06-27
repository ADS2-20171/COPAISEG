from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (PagoPersonalListView, PagoPersonalCreateView,
                    PagoPersonalUpdateView, PagoPersonalDeleteView,
                    )
from . import views


urlpatterns = [
    # url(r'$', IndexView.as_view(), name="index"),

    # URLS PERSONA
    url(r'^pagopersonal/listar/$',
        login_required(PagoPersonalListView.as_view()), name="pagopersonal_list"),
    url(r'^pagopersonal/crear/$',
        login_required(PagoPersonalCreateView.as_view()), name="pagopersonal_add"),
    url(r'^pagopersonal/editar/(?P<pk>[^/]+)$',
        login_required(PagoPersonalUpdateView.as_view()), name='pagopersonal_update'),
    url(r'^pagopersonal/eliminar/(?P<pk>[^/]+)$',
        login_required(PagoPersonalDeleteView.as_view()), name='pagopersonal_delete'),
]
