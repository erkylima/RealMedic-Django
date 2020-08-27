from django.urls import path

from core.modulos.atendimentos_departamento.views_atendimentos_departamento import *

app_name = 'atendimentos_departamento'

urlpatterns = [
    path('list', AtendimentosDepartamentoListView.as_view(), name='list_view'),
    path('create', AtendimentosDepartamentoCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', AtendimentosDepartamentoUpdateView.as_view(), name='update_view'),
    path('getTipoProfissionalPorIdTipoAtendimento/<int:idTipoAtendimento>', getTipoProfissionalPorIdTipoAtendimento,
         name='getTiposAtendimentosPorIdTipoProfissional'),
]
