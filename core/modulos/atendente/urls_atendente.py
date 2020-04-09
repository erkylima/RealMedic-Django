from django.urls import path

from core.modulos.atendente import views_atendente

app_name = 'atendente'
urlpatterns = [
    path('list', views_atendente.AtendenteListView.as_view(), name='list_view'),
    path('create', views_atendente.AtendenteCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_atendente.AtendenteUpdateView.as_view(), name='update_view'),
]
