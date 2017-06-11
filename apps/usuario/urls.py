from django.conf.urls import url
from .views import RegistroUsuario

urlpatterns = [
    url(r'^registrar$', RegistroUsuario.as_view(), name='acopio_list'),
    # url(r'^post/crear/', PostCreateView.as_view(), name='post_add'),
    # url(r'^post/actualizar/(?P<pk>[^/]+)$', PostUpdateView.as_view(), name='post_update'),
    # url(r'^post/eliminar/(?P<pk>[^/]+)$', PostDeleteView.as_view(), name='post_delete'),

]
