from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Paciente
from core.modulos.paciente.form_paciente import PacienteForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('core:modulo:paciente:list_view')
    search_fields = ['nome']
    COLUMNS = [LabesProperty.NOME]
    NAME_MODEL = Paciente._meta.verbose_name
    NAME_MODEL_PLURAL = Paciente._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:paciente:create_view')

class MyListViewPaciente(MyGenericView, LoginRequiredMixin,
                            MyListViewSearcheGeneric,
                            MyLabls,
                            ListView):
    allow_empty = True
    paginate_by = 10

    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'


class MyCreateViewPaciente(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewPaciente(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class PacienteListView(MyListViewPaciente):
    template_name = 'paciente/templates/list_view_paciente.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class PacienteCreateView(MyCreateViewPaciente):
    template_name = 'paciente/templates/create_view_paciente.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(PacienteCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        form.save(commit=False)
        return super().form_valid(form)


class PacienteUpdateView(MyUpdateViewPaciente):
    template_name = 'paciente/templates/create_view_paciente.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(PacienteUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)
