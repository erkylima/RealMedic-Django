from django.urls import path

from core.modulos.tipo_profissional import views_tipo_profissional

app_name = 'tipo_profissional'

urlpatterns = [
    path('list', views_tipo_profissional.TipoProfissionalListView.as_view(), name='list_view'),
    path('create', views_tipo_profissional.TipoProfissionalCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_tipo_profissional.TipoProfissionalUpdateView.as_view(), name='update_view'),
    path('getTipoProfissionalPorIdDepartamento/<int:idDepartamento>', views_tipo_profissional.getTipoProfissionalPorIdDepartamento,
         name='getTipoProfissionalPorIdDepartamento'),

]
