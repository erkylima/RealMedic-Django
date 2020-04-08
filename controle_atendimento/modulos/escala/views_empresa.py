from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Empresa
from core.modulos.empresa.form_empresa import EmpresaForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


#PermissionRequiredMixin
class MyListViewEmpresa(LoginRequiredMixin,  MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True
    paginate_by = 10
    # permission_required = 'core.view_empresa'
    # permission_denied_message = 'Acesso Negado'

    # def handle_no_permission(self):
    #     print(self.request.user.get_user_permissions())
    #     print(self.request.user.username)
    #     for i in Permission.objects.all():
    #         print(i.codename)
    #     messages.error(self.request, 'You don\'t have permission to do this')
    #     return super(MyListViewEmpresa, self).handle_no_permission()


class MyCreateViewEmpresa(LoginRequiredMixin, MyLabls, CreateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewEmpresa(LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class EmpresaListView(MyListViewEmpresa):
    template_name = 'empresa/templates/list_view_empresa.html'
    model = Empresa
    search_fields = ['nome_razao_social', 'documento']


    COLUMNS = [LabesProperty.NOME, LabesProperty.DOCUMENTO]
    NAME_MODEL = Empresa._meta.verbose_name
    NAME_MODEL_PLURAL = Empresa._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:empresa:create_view')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context




class EmpresaCreateView(MyCreateViewEmpresa):
    template_name = 'empresa/templates/create_view_empresa.html'
    model = Empresa
    form_class = EmpresaForm
    success_url = reverse_lazy('core:modulo:empresa:list_view')

    NAME_MODEL = Empresa._meta.verbose_name

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(EmpresaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class EmpresaUpdateView(MyUpdateViewEmpresa):
    template_name = 'empresa/templates/create_view_empresa.html'
    model = Empresa
    form_class = EmpresaForm
    success_url = reverse_lazy('core:modulo:empresa:list_view')
    NAME_MODEL = Empresa._meta.verbose_name

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(EmpresaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)
