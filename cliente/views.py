from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from cliente.models import ContactForm, Contact
from cliente.modulos.landingpage.ListaProfissional import ListaProfissional, ListaEmpresa
from core.modulos.tipo_profissional.tipo_profissional import TipoProfissional


class IndexTest(TemplateView):
    template_name = 'landingpage/indextest.html'

class ListaProfissionalListView(TemplateView):
    template_name ='landingpage/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListaProfissionalListView, self).get_context_data(**kwargs)
        context['empresas'] = ListaEmpresa.objects.filter(pais__nome__icontains="Brasil").order_by('?')
        context['cidade'] = 'Floresta-PE'
        context['especialidades'] = TipoProfissional.objects.all().order_by('descricao')
        pesquisa = self.request.GET.get('q')
        context['pesquisa'] = str(pesquisa)
        if (pesquisa != None):
            context['lista'] = ListaProfissional.objects.filter(especi__descricao__icontains=str(pesquisa),
                                                                listaempresa__pais__nome__icontains='Brasil', ativo=True).order_by('?')
        else:
            context['lista'] = ListaProfissional.objects.filter(listaempresa__pais__nome__icontains='Brasil', ativo=True).order_by('?')
        return context

class ListaProfissionalAngolaListView(TemplateView):
    template_name ='landingpage/index.html'

    def get_context_data(self, **kwargs):
        context = super(ListaProfissionalAngolaListView, self).get_context_data(**kwargs)
        context['empresas'] = ListaEmpresa.objects.filter(pais__nome__icontains="Angola").order_by('?')
        context['municipio'] = 'Luanda-LU'
        print(ListaEmpresa.objects.filter(pais__nome__icontains="Angola").order_by('?'))
        context['especialidades'] = TipoProfissional.objects.all().order_by('descricao')
        pesquisa = self.request.GET.get('q')
        context['pesquisa'] = str(pesquisa)
        if (pesquisa != None):
            context['lista'] = ListaProfissional.objects.filter(especi__descricao__icontains=str(pesquisa),
                                                                listaempresa__pais__nome__icontains='Angola').order_by('?')
        else:
            context['lista'] = ListaProfissional.objects.filter(listaempresa__pais__nome__icontains='Angola').order_by('?')
        return context




class SobreListView(TemplateView):
    template_name ='landingpage/about.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contato = Contact.objects.get_or_create(email=request.POST.get('email'))
            contato = Contact.objects.get(email=request.POST.get('email'))
            contato.name = request.POST.get('name')
            contato.save()
            messages.success(request, 'Que bom que você deseja tornar a saúde mais acessível! Entraremos em contato em breve.')
        else:
            messages.error(request, 'Preencha todos os campos.')
        return redirect("core:cliente:sobre")
    