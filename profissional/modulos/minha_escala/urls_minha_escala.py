from django.urls import path

from profissional.modulos.minha_escala import views_minha_escala

app_name = 'minha_escala'
urlpatterns = [
    path('update/', views_minha_escala.MinhaEscalaUpdateView.as_view(), name='update_view'),
]
