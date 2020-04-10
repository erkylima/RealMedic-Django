from django.urls import path

from core.modulos.profissional import views_profissional

app_name = 'profissional'
urlpatterns = [
    path('list', views_profissional.ProfissionalListView.as_view(), name='list_view'),
    path('create', views_profissional.ProfissionalCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_profissional.ProfissionalUpdateView.as_view(), name='update_view'),

    path('getDepartamentoIdEmpresa/<int:idEmpresa>', views_profissional.getDepartamentosPorIdEmpresa, name='getDepartamentosPorIdEmpresa'),

]
