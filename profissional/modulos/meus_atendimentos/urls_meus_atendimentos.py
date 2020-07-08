from django.urls import path

from profissional.modulos.meus_atendimentos.views_meus_atendimentos import *
app_name = 'meus_atendimentos'

urlpatterns = [
    path('list/', MeusAtendimentosListView.as_view(), name='list_view'),


]
