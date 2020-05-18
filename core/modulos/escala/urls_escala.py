from django.urls import path

from core.modulos.escala import views_escala

app_name = 'escala'
urlpatterns = [
    path('create', views_escala.EscalaCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_escala.EscalaUpdateView.as_view(), name='update_view'),
    path('add_edit_escala/', views_escala.addEditEscala, name="add_edit_escala"),
    path('marcar/', views_escala.marcarMes, name="marcar"),

]
