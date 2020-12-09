from django.urls import path

from core.modulos.convenio.views_convenio import ConvenioListView, ConvenioCreateView, ConvenioUpdateView

app_name = 'tipo_profissional'

urlpatterns = [
    path('list', ConvenioListView.as_view(), name='list_view'),
    path('create', ConvenioCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', ConvenioUpdateView.as_view(), name='update_view'),


]
