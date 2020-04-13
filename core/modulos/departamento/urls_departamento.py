from django.urls import path

from core.modulos.departamento import views_departamento

app_name = 'departamento'
urlpatterns = [
    path('list', views_departamento.DepartamentoListView.as_view(), name='list_view'),
    path('create', views_departamento.DepartamentoCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_departamento.DepartamentoUpdateView.as_view(), name='update_view'),
    path('getDepartamentoIdEmpresa/<int:idEmpresa>', views_departamento.getDepartamentosPorIdEmpresa, name='getDepartamentosPorIdEmpresa'),

]
