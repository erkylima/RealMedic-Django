from django.urls import path

from profissional.modulos.relatorio.views_relatorio import RelatorioView

app_name = 'relatorio'
urlpatterns = [
    path('', RelatorioView.as_view(), name='ver'),
]
