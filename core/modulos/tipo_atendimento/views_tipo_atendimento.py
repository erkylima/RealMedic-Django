from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from core.models import TipoAtendimento
from core.modulos.tipo_atendimento.form_tipo_atendimento import TipoAtendimentoForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = TipoAtendimento
    form_class = TipoAtendimentoForm
    success_url = reverse_lazy('core:modulo:tipo_atendimento:list_view')
    search_fields = ['descricao']
    COLUMNS = [LabesProperty.DESCRICAO]
    NAME_MODEL = TipoAtendimento._meta.verbose_name
    NAME_MODEL_PLURAL = TipoAtendimento._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:tipo_atendimento:create_view')


class MyListViewTipoAtendimento(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True


class MyCreateViewTipoAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewTipoAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class TipoAtendimentoListView(MyListViewTipoAtendimento):
    template_name = 'tipo_atendimento/templates/list_view_tipo_atendimento.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def get_queryset(self):
        return super().get_queryset()

    @method_decorator(permission_required(['global_permissions.ver_tipos_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TipoAtendimentoListView, self).dispatch(*args, **kwargs)

class TipoAtendimentoCreateView(MyCreateViewTipoAtendimento):
    template_name = 'tipo_atendimento/templates/create_view_tipo_atendimento.html'


    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(TipoAtendimentoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        form.save(commit=False)

        return super().form_valid(form)


class TipoAtendimentoUpdateView(MyUpdateViewTipoAtendimento):
    template_name = 'tipo_atendimento/templates/create_view_tipo_atendimento.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(TipoAtendimentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)

@login_required()
def getTiposAtendimentosPorIdTipoProfissional(request, idTipoProfissional):
    subs = {}
    departamentos = TipoAtendimento.objects.filter(tipo_profissional_id=idTipoProfissional)

    for dep in departamentos:
        subs[dep.id] = dep.descricao
    return JsonResponse(subs)
