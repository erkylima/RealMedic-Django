from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Departamento
from core.modulos.departamento.form_departamento import DepartamentoForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('core:modulo:departamento:list_view')
    search_fields = ['nome', 'descricao']
    COLUMNS = [LabesProperty.NOME, LabesProperty.DESCRICAO]
    NAME_MODEL = Departamento._meta.verbose_name
    NAME_MODEL_PLURAL = Departamento._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:departamento:create_view')


class MyListViewDepartamento(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True


class MyCreateViewDepartamento(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewDepartamento(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    pass


class DepartamentoListView(MyListViewDepartamento):
    template_name = 'departamento/templates/list_view_departamento.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    @method_decorator(permission_required(['global_permissions.ver_departamentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(DepartamentoListView, self).dispatch(*args, **kwargs)

class DepartamentoCreateView(MyCreateViewDepartamento):
    template_name = 'departamento/templates/create_view_departamento.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(DepartamentoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_departamentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(DepartamentoCreateView, self).dispatch(*args, **kwargs)

class DepartamentoUpdateView(MyUpdateViewDepartamento):
    template_name = 'departamento/templates/create_view_departamento.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(DepartamentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_departamentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(DepartamentoUpdateView, self).dispatch(*args, **kwargs)

@login_required()
def getDepartamentosPorIdEmpresa(request, idEmpresa):
    subs = {}
    departamentos = Departamento.objects.filter(empresa_id=idEmpresa)

    for dep in departamentos:
        subs[dep.id] = dep.nome
    return JsonResponse(subs)
