
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from cliente.modulos.landingpage import ListaProfissional


class ListaProfissionalListView(TemplateView):
    template_name ='landingpage/index.html'

class SobreListView(TemplateView):
    template_name ='landingpage/about.html'
