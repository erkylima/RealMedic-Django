from django.urls import path

from profissional.modulos.prontuario.views_prontuario import ProntuarioCreateView, ProntuarioUpdateView

app_name = 'prontuario'
urlpatterns = [
    path('create/<int:pk>', ProntuarioCreateView.as_view(), name='create_view'),
    path('update/<int:prontuariopaciente>/<int:pk>/', ProntuarioUpdateView.as_view(), name='update_view'),
]
