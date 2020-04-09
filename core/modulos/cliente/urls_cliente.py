from django.urls import path

from core.modulos.cliente import views_cliente

app_name = 'cliente'
urlpatterns = [
    path('list', views_cliente.ClienteListView.as_view(), name='list_view'),
    path('create', views_cliente.ClienteCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_cliente.ClienteUpdateView.as_view(), name='update_view'),
]
