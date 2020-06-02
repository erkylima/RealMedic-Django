from django.urls import path

from core.modulos.atendimento import views_atendimento

app_name = 'atendimento'
urlpatterns = [
    path('detail/<int:pk>', views_atendimento.AtendimentoListView.as_view(), name='detail_view'),
    path('list', views_atendimento.AtendimentoListView.as_view(), name='list_view'),
    path('create', views_atendimento.AtendimentoCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_atendimento.AtendimentoUpdateView.as_view(), name='update_view'),
    path('add_atendimento', views_atendimento.addAtendimento, name="add_atendimento"),
    path('desmarcar_atendimento', views_atendimento.desmarcarAtendimento, name="desmarcar_atendimento"),
]
