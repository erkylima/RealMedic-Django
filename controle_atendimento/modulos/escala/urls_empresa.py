from django.urls import path

from core.modulos.empresa import views_empresa

app_name = 'empresa'
urlpatterns = [
    path('list', views_empresa.EmpresaListView.as_view(), name='list_view'),
    path('create', views_empresa.EmpresaCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_empresa.EmpresaUpdateView.as_view(), name='update_view'),
]
