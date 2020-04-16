from django.urls import path

from core.modulos.escala import views_escala

app_name = 'escala'
urlpatterns = [
    path('list', views_escala.EscalaListView.as_view(), name='list_view'),
    path('create', views_escala.EscalaCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_escala.EscalaUpdateView.as_view(), name='update_view'),
]
