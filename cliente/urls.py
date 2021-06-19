from django.urls import path, include

from cliente.views import ListaProfissionalListView, SobreListView, contact, ListaProfissionalAngolaListView, IndexTest, \
    ProfissionalDetail
from core import views_core

app_name = 'cliente'
urlpatterns = [
    # path('/', include('cliente.modulos.urls')),
    path('', ListaProfissionalListView.as_view(), name="lista_prof"),
    path('profissional/<int:pk>',ProfissionalDetail.as_view(), name="profissional"),
    path('ao', ListaProfissionalAngolaListView.as_view(), name="lista_angola"),
    path('sobre', SobreListView.as_view(), name="sobre"),
    path('contato',contact,name='contato'),
    path('indextest', IndexTest.as_view(), name="teste"),
]
