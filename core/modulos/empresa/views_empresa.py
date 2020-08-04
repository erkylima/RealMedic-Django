from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Empresa
from core.modulos.empresa.form_empresa import EmpresaForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = Empresa
    form_class = EmpresaForm
    success_url = reverse_lazy('core:modulo:empresa:list_view')
    search_fields = ['nome_razao_social', 'documento']
    COLUMNS = [LabesProperty.NOME, LabesProperty.DOCUMENTO]
    NAME_MODEL = Empresa._meta.verbose_name
    NAME_MODEL_PLURAL = Empresa._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:empresa:create_view')


class MyListViewEmpresa(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True


class MyCreateViewEmpresa(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewEmpresa(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class EmpresaListView(MyListViewEmpresa):
    template_name = 'empresa/templates/list_view_empresa.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def get_queryset(self):
        return super().get_queryset()

    @method_decorator(permission_required(['global_permissions.ver_empresas'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(EmpresaListView, self).dispatch(*args, **kwargs)

class EmpresaCreateView(MyCreateViewEmpresa):
    template_name = 'empresa/templates/create_view_empresa.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(EmpresaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class EmpresaUpdateView(MyUpdateViewEmpresa):
    template_name = 'empresa/templates/create_view_empresa.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(EmpresaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)
