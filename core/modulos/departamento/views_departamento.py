from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.urls import reverse_lazy
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
    COLUMNS = [LabesProperty.NOME, LabesProperty.DOCUMENTO]
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


class DepartamentoCreateView(MyCreateViewDepartamento):
    template_name = 'departamento/templates/create_view_departamento.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(DepartamentoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class DepartamentoUpdateView(MyUpdateViewDepartamento):
    template_name = 'departamento/templates/create_view_departamento.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(DepartamentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)
