from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Paciente
from core.modulos.paciente.form_paciente import PacienteForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa


class MyGenericView(object):
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('core:modulo:paciente:list_view')
    search_fields = ['nome']
    COLUMNS = [LabesProperty.NOME, LabesProperty.DEPARTAMENTO]
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


class MyUpdateViewPaciente(MyGenericView, LoginRequiredMixin, ValidarEmpresa, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class PacienteListView(MyListViewPaciente):
    template_name = 'paciente/templates/list_view_paciente.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def get_queryset(self):
        try:
            if (self.request.GET.get('q')):
                queryset = Paciente.objects.filter(Q(nome__icontains=self.request.GET.get('q')) & Q(departamento_id=self.request.user.userAtendente.departamento_id))
            else:
                queryset = Paciente.objects.filter(departamento_id=self.request.user.userAtendente.departamento_id)
        except:
            if (self.request.GET.get('q')):
                queryset = Paciente.objects.filter(Q(nome__icontains=self.request.GET.get('q')) & Q(departamento__empresa_id=self.request.user.userProfile.empresa_id))
            else:
                queryset = Paciente.objects.filter(departamento__empresa_id=self.request.user.userProfile.empresa_id)
        return queryset

    @method_decorator(permission_required(['global_permissions.ver_pacientes'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(PacienteListView, self).dispatch(*args, **kwargs)

class PacienteCreateView(MyCreateViewPaciente):
    template_name = 'paciente/templates/create_view_paciente.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))

        return super(PacienteCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        paciente = form.save(commit=False)
        try:
            if self.request.user.userAtendente:
                paciente.departamento_id = self.request.user.userAtendente.departamento_id
        except:
            if self.request.user.userProfile:
                paciente.departamento_id = self.request.POST.get('departamento')
        form.save(commit=False)
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_pacientes'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(PacienteCreateView, self).dispatch(*args, **kwargs)

class PacienteUpdateView(MyUpdateViewPaciente):
    template_name = 'paciente/templates/create_view_paciente.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.object.pk)
        try:
            context['paciente'] = Paciente.objects.get(pk=self.object.pk, departamento_id=self.request.user.userAtendente.departamento_id)
        except:
            try:
                context['paciente'] = Paciente.objects.get(pk=self.object.pk, departamento__empresa_id=self.request.user.userProfile.empresa_id)
            except:
                pass

        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(PacienteUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        paciente = form.save(commit=False)
        try:
            if self.request.user.userAtendente:
                paciente.departamento_id = self.request.user.userAtendente.departamento_id
        except:
            if self.request.user.userProfile:
                paciente.departamento_id = self.request.POST.get('departamento')
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_pacientes'], raise_exception=True))
    def dispatch(self, *args, **kwargs):            
        return super(PacienteUpdateView, self).dispatch(*args, **kwargs)