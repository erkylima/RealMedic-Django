
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from cliente.modulos.landingpage.ListaProfissional import ListaProfissional


class ListaProfissionalListView(TemplateView):
    template_name ='landingpage/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListaProfissionalListView, self).get_context_data(**kwargs)
        context['lista'] = ListaProfissional.objects.all().order_by('?')

        return context




class SobreListView(TemplateView):
    template_name ='landingpage/about.html'
