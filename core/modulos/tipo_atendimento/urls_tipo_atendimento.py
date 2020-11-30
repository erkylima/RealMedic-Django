from django.urls import path

from core.modulos.tipo_atendimento import views_tipo_atendimento

app_name = 'tipo_atendimento'

urlpatterns = [
    path('list', views_tipo_atendimento.TipoAtendimentoListView.as_view(), name='list_view'),
    path('create', views_tipo_atendimento.TipoAtendimentoCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_tipo_atendimento.TipoAtendimentoUpdateView.as_view(), name='update_view'),
    path('getTiposAtendimentosPorIdTipoProfissional/<int:idTipoProfissional>/<int:idDepartamento>/', views_tipo_atendimento.getTiposAtendimentosPorIdTipoProfissional,
         name='getTiposAtendimentosPorIdTipoProfissional'),
]
