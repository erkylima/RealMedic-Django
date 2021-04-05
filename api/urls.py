from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path("usuario/", include('api.modulos.usuario.urls')),
    path("profissional/", include('api.modulos.profissional.urls')),

]
