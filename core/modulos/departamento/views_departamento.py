from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Departamento
from core.modulos.departamento.form_departamento import DepartamentoForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


#PermissionRequiredMixin
class MyListViewDepartamento(LoginRequiredMixin,  MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True
    paginate_by = 10
    # permission_required = 'core.view_departamento'
    # permission_denied_message = 'Acesso Negado'

    # def handle_no_permission(self):
    #     print(self.request.user.get_user_permissions())
    #     print(self.request.user.username)
    #     for i in Permission.objects.all():
    #         print(i.codename)
    #     messages.error(self.request, 'You don\'t have permission to do this')
    #     return super(MyListViewDepartamento, self).handle_no_permission()


class MyCreateViewDepartamento(LoginRequiredMixin, MyLabls, CreateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewDepartamento(LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class DepartamentoListView(MyListViewDepartamento):
    template_name = 'departamento/templates/list_view_departamento.html'
    model = Departamento
    search_fields = ['nome', 'descricao']


    COLUMNS = [LabesProperty.NOME, LabesProperty.DOCUMENTO]
    NAME_MODEL = Departamento._meta.verbose_name
    NAME_MODEL_PLURAL = Departamento._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:departamento:create_view')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context




class DepartamentoCreateView(MyCreateViewDepartamento):
    template_name = 'departamento/templates/create_view_departamento.html'
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('core:modulo:departamento:list_view')

    NAME_MODEL = Departamento._meta.verbose_name

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(DepartamentoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class DepartamentoUpdateView(MyUpdateViewDepartamento):
    template_name = 'departamento/templates/create_view_departamento.html'
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('core:modulo:departamento:list_view')
    NAME_MODEL = Departamento._meta.verbose_name

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(DepartamentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)
