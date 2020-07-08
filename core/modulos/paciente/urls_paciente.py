from django.urls import path

from core.modulos.paciente import views_paciente

app_name = 'paciente'
urlpatterns = [
    path('list', views_paciente.PacienteListView.as_view(), name='list_view'),
    path('create', views_paciente.PacienteCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_paciente.PacienteUpdateView.as_view(), name='update_view'),
]
