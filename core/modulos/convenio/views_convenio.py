from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Convenio
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento
from core.modulos.convenio.form_convenio import ConvenioForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa


class MyGenericView(object):
    model = Convenio
    form_class = ConvenioForm
    success_url = reverse_lazy('core:modulo:tipo_profissional:list_view')
    search_fields = ['descricao']
    COLUMNS = [LabesProperty.DESCRICAO]
    NAME_MODEL = Convenio._meta.verbose_name
    NAME_MODEL_PLURAL = Convenio._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:tipo_profissional:create_view')


class MyListViewConvenio(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True


class MyCreateViewConvenio(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewConvenio(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class ConvenioListView(MyListViewConvenio):
    template_name = 'tipo_profissional/templates/list_view_tipo_profissional.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def get_queryset(self):
        return super().get_queryset()

    @method_decorator(permission_required(['global_permissions.ver_tipos_profissional'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ConvenioListView, self).dispatch(*args, **kwargs)

class ConvenioCreateView(MyCreateViewConvenio):
    template_name = 'tipo_profissional/templates/create_view_tipo_profissional.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ConvenioCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_tipos_profissional'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ConvenioCreateView , self).dispatch(*args, **kwargs)

class ConvenioUpdateView(MyUpdateViewConvenio):
    template_name = 'tipo_profissional/templates/create_view_tipo_profissional.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ConvenioUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_tipos_profissional'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ConvenioUpdateView, self).dispatch(*args, **kwargs)
