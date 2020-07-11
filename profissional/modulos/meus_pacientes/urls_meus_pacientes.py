from django.urls import path

from profissional.modulos.meus_pacientes.views_meus_pacientes import *
app_name = 'meus_pacientes'

urlpatterns = [
    path('list/', MeusPacientesListView.as_view(), name='list_view'),
    path('detalhe/<int:pk>', MeusPacientesDetalheView.as_view(), name='detalhe_view'),

]
