from django.urls import path, include

from core import views_core

app_name = 'cliente'
urlpatterns = [
    path('cliente/', include('cliente.modulos.urls'))
]
