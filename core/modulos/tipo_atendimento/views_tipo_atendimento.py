from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from core.models import TipoAtendimento
from core.modulos.atendimentos_departamento.atendimentos_departamento import AtendimentosDepartamento
from core.modulos.departamento.departamento import Departamento
from core.modulos.tipo_atendimento.form_tipo_atendimento import TipoAtendimentoForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa


class MyGenericView(object):
    model = TipoAtendimento
    form_class = TipoAtendimentoForm
    success_url = reverse_lazy('core:modulo:tipo_atendimento:list_view')
    search_fields = ['descricao']
    COLUMNS = [LabesProperty.DESCRICAO, LabesProperty.DEPARTAMENTO]
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
        if (self.request.GET.get('q')):
            queryset = TipoAtendimento.objects.filter(Q(descricao__icontains=self.request.GET.get('q')) )
        else:
            queryset = TipoAtendimento.objects.all()
        return queryset

    @method_decorator(permission_required(['global_permissions.ver_tipos_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TipoAtendimentoListView, self).dispatch(*args, **kwargs)

class TipoAtendimentoCreateView(MyCreateViewTipoAtendimento):
    template_name = 'tipo_atendimento/templates/create_view_tipo_atendimento.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(TipoAtendimentoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        print("teste")
        form.save(commit=False)

        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_tipos_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TipoAtendimentoCreateView, self).dispatch(*args, **kwargs)

class TipoAtendimentoUpdateView(MyUpdateViewTipoAtendimento):
    template_name = 'tipo_atendimento/templates/create_view_tipo_atendimento.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(TipoAtendimentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_tipos_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TipoAtendimentoUpdateView, self).dispatch(*args, **kwargs)

@login_required()
def getTiposAtendimentosPorIdTipoProfissional(request, idTipoProfissional, idDepartamento):
    subs = {}
    tipos_atendimentos = AtendimentosDepartamento.objects.filter(tipo_atendimento__tipo_profissional=idTipoProfissional,departamento_id=idDepartamento)
    for dep in tipos_atendimentos:
        subs[dep.id] = dep.tipo_atendimento.descricao

    return JsonResponse(subs)
