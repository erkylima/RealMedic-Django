from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.models import TipoProfissional
from core.modulos.tipo_profissional.form_tipo_profissional import TipoProfissionalForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = TipoProfissional
    form_class = TipoProfissionalForm
    success_url = reverse_lazy('core:modulo:tipo_profissional:list_view')
    search_fields = ['descricao']
    COLUMNS = [LabesProperty.DESCRICAO]
    NAME_MODEL = TipoProfissional._meta.verbose_name
    NAME_MODEL_PLURAL = TipoProfissional._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:tipo_profissional:create_view')


class MyListViewTipoProfissional(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True


class MyCreateViewTipoProfissional(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewTipoProfissional(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class TipoProfissionalListView(MyListViewTipoProfissional):
    template_name = 'tipo_profissional/templates/list_view_tipo_profissional.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def get_queryset(self):
        return super().get_queryset()


class TipoProfissionalCreateView(MyCreateViewTipoProfissional):
    template_name = 'tipo_profissional/templates/create_view_tipo_profissional.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(TipoProfissionalCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class TipoProfissionalUpdateView(MyUpdateViewTipoProfissional):
    template_name = 'tipo_profissional/templates/create_view_tipo_profissional.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(TipoProfissionalUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)


@login_required()
def getTipoProfissionalPorIdDepartamento(request, idDepartamento):
    subs = {}
    tipoprofissional = TipoProfissional.objects.filter(departamento_id=idDepartamento)
    for dep in tipoprofissional:
        subs[dep.id] = dep.descricao
    return JsonResponse(subs)