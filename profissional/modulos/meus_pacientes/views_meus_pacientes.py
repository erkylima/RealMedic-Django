

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView

from core.models import Paciente, Prontuario

from core.modulos.paciente.paciente import PacienteDepartamentoProfissional
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls
from profissional.modulos.meus_pacientes.form_meus_pacientes import MeusPacientesForm


class MyGenericView(object):
    model = PacienteDepartamentoProfissional
    form_class = MeusPacientesForm
    success_url = reverse_lazy('profissional:modulo:meus_pacientes:list_view')
    search_fields = ['nome','email']
    COLUMNS = [LabesProperty.NOME, LabesProperty.EMAIL]
    NAME_MODEL = Paciente._meta.verbose_name
    NAME_MODEL_PLURAL = Paciente._meta.verbose_name_plural
    # PAGE_CREATE_VIEW = reverse_lazy('profissional:modulo:meus_pacientes:list_view')


class MyListViewMeusPacientes(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True

class MyDetalheViewMeusPacientes(MyGenericView, LoginRequiredMixin, MyLabls, DetailView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass

class MyUpdateViewMeusPacientes(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass

class MeusPacientesListView(MyListViewMeusPacientes):
    template_name = 'meus_pacientes/templates/list_view_meus_pacientes.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        return context
    def get_queryset(self):
        queryset = PacienteDepartamentoProfissional.objects.filter(departamentoProfissional_id=self.request.user.userProfissional.pk)
        return queryset

class MeusPacientesDetalheView(MyDetalheViewMeusPacientes):
    template_name = 'meus_pacientes/templates/detalhe_view_meus_pacientes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prontuarios = Prontuario.objects.filter(departamento_profissional_paciente__paciente=self.object.pk)

        for pro in prontuarios:
            print(pro.getListAtributes)
        context['prontuarios'] = prontuarios
        return context

class MeusPacientesUpdateView(MyUpdateViewMeusPacientes):
    template_name = 'meus_pacientes/templates/detalhe_view_meus_pacientes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # prontuario = Prontuario.objects.filter(departamento_profissional_paciente=self.object.pk)

        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(MeusPacientesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)

