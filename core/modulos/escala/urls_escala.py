from django.urls import path

from core.modulos.escala import views_escala

app_name = 'escala'
urlpatterns = [
    path('add_edit_escala/', views_escala.addEditEscala, name="add_edit_escala"),
    path('limpar/', views_escala.limparIntervalo, name="limpar_intervalo"),
    path('limpardia/', views_escala.limparIntervaloDia, name="limpar_intervalo_dia"),

]
