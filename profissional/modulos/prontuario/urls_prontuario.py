from django.urls import path

from profissional.modulos.prontuario.views_prontuario import ProntuarioCreateView, ProntuarioUpdateView

app_name = 'prontuario'
urlpatterns = [
    path('create', ProntuarioCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', ProntuarioUpdateView.as_view(), name='update_view'),
]
