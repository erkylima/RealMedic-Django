from django.urls import path

from profissional.modulos.prontuario.views_prontuario import ProntuarioCreateView, ProntuarioUpdateView

app_name = 'prontuario'
urlpatterns = [
    path('update/<int:prontuariopaciente>/<int:pk>/', ProntuarioUpdateView.as_view(), name='update_view'),
]
