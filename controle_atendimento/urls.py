from django.urls import path, include

from core import views_core

app_name = 'cotrole_atendimento'
urlpatterns = [
    path('cotrole_atendimento/', include('controle_atendimento.modulos.urls')),
]
