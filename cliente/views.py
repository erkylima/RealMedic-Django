
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from cliente.modulos.landingpage.ListaProfissional import ListaProfissional, ListaEmpresa
from core.modulos.tipo_profissional.tipo_profissional import TipoProfissional


class ListaProfissionalListView(TemplateView):
    template_name ='landingpage/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListaProfissionalListView, self).get_context_data(**kwargs)
        context['empresas'] = ListaEmpresa.objects.all().order_by('?')
        context['especialidades'] = TipoProfissional.objects.all().order_by('descricao')
        pesquisa = self.request.GET.get('q')
        context['pesquisa'] = str(pesquisa)
        print(str(pesquisa))
        if(pesquisa!=None):
            context['lista'] = ListaProfissional.objects.all().order_by('?').filter(especi__descricao__icontains=str(pesquisa))
        else:
            context['lista'] = ListaProfissional.objects.all().order_by('?')
        return context




class SobreListView(TemplateView):
    template_name ='landingpage/about.html'
