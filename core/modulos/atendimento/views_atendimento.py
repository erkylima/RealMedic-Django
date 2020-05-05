from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.views.generic.base import View

from core.models import Atendimento, DepartamentoProfissional, Profissional, Escala
from core.modulos.atendimento.form_atendimento import AtendimentoForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = DepartamentoProfissional
    form_class = AtendimentoForm
    success_url = reverse_lazy('core:modulo:atendimento:list_view')
    search_fields = ['nome_razao_social', 'documento']
    COLUMNS = [LabesProperty.NOME, LabesProperty.DOCUMENTO]
    NAME_MODEL = Atendimento._meta.verbose_name
    NAME_MODEL_PLURAL = Atendimento._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:atendimento:create_view')


class MyListViewAtendimento(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True

class MyDetailViewAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, View):
    pass

class MyCreateViewAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass

class AtendimentoDetailView(MyDetailViewAtendimento):
    template_name = 'atendimento/templates/list_view_atendimento.html'


class AtendimentoListView(MyListViewAtendimento):
    template_name = 'atendimento/templates/list_view_atendimento.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        atendimentos = []
        for prof in context['departamentoprofissional_list']:
            atendimento = Atendimento.objects.filter(departamentoProfissional_id=prof.pk)
            atendimentos.append(atendimento)
        # print(context['departamentoprofissional_list'][0].tipo_profissional)
        # print(context['departamentoprofissional_list'][0].profissional.tiposAtendimentos.values_list)
        # print(atendimentos[0].last().escalaIntervalo)
        context['atendimentos'] = atendimentos
        # context['profissionais'] = DepartamentoProfissional.objects.select_related('')
        # print(dir(context['profissionais'][1].tipo_profissional))
        # # print(context)
        return context



class AtendimentoCreateView(MyCreateViewAtendimento):
    template_name = 'atendimento/templates/create_view_atendimento.html'
    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendimentoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class AtendimentoUpdateView(MyUpdateViewAtendimento):
    template_name = 'atendimento/templates/create_view_atendimento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional = Profissional.objects.get(pk=self.object.pk)
        context['profissional'] = profissional

        escalas = Escala.objects.filter(departamentoProfissional_id=self.object.pk)
        intervalos = []
        for escala in escalas:
            intervalo = escala.escalaintervalo_set.get(escala_id=escala.pk)

            b = {'id': escala.pk,
                 'title': profissional.nome,
                 'start': str(escala.dia) + "T" + str(intervalo.inicio),
                 'end': str(escala.dia) + "T" + str(intervalo.fim),
                 'description': intervalo.descricao,
                 'className': "fc-" + intervalo.cor
                 }
            intervalos.append(b)
        print(intervalos)
        context['intervalos'] = intervalos
        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendimentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)
