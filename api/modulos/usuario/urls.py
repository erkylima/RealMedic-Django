from django.urls import path

from api.modulos.usuario.views import *

urlpatterns = [
    path("create/", UsuarioCreateView.as_view(), name="create"),
    path("list/", UsuarioListView.as_view(), name="list"),
    path("get/", UsuarioGetView.as_view(), name="post"),
    #path("getToken/<int:pk>", UsuarioTokenGetView.as_view(), name="getToken"),
]
