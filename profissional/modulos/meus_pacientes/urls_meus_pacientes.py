from django.urls import path

from profissional.modulos.meus_pacientes import views_meus_pacientes

app_name = 'meus_pacientes'
urlpatterns = [
    path('list/', views_meus_pacientes.MeusPacientesListView.as_view(), name='list_view'),
    path('detalhe/<int:pk>', views_meus_pacientes.MeusPacientesDetalheView.as_view(), name='detalhe_view'),
]

