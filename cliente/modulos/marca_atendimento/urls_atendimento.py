from django.urls import path

from cliente.modulos.marca_atendimento.views_atendimento import *
app_name = 'marca_atendimento'
urlpatterns = [
    path('list/', AtendimentoListView.as_view(), name='list_view'),
    path('update/<int:pk>', AtendimentoUpdateView.as_view(), name='update_view'),
    path('add_atendimento', addAtendimento, name="add_atendimento"),
    path('desmarcar_atendimento', desmarcarAtendimento, name="desmarcar_atendimento"),
]
