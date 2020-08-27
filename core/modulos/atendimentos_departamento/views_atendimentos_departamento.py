from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from core.models import TipoAtendimento
from core.modulos.atendimentos_departamento.atendimentos_departamento import AtendimentosDepartamento
from core.modulos.atendimentos_departamento.form_atendimentos_departamento import AtendimentosDepartamentoForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa


class MyGenericView(object):
    model = AtendimentosDepartamento
    form_class = AtendimentosDepartamentoForm
    success_url = reverse_lazy('core:modulo:atendimentos_departamento:list_view')
    search_fields = ['descricao']
    COLUMNS = [LabesProperty.DESCRICAO, LabesProperty.DEPARTAMENTO]
    NAME_MODEL = AtendimentosDepartamento._meta.verbose_name
    NAME_MODEL_PLURAL = AtendimentosDepartamento._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:atendimentos_departamento:create_view')


class MyListViewAtendimentosDepartamento(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True


class MyCreateViewAtendimentosDepartamento(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewAtendimentosDepartamento(MyGenericView, LoginRequiredMixin, ValidarEmpresa, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class AtendimentosDepartamentoListView(MyListViewAtendimentosDepartamento):
    template_name = 'atendimentos_departamento/templates/list_view_atendimentos_departamento.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        print(context)
        return context

    # def get_queryset(self):
    #     if (self.request.GET.get('q')):
    #         queryset = AtendimentosDepartamento.objects.filter(Q(tipo_atendimento__descricao__icontains=self.request.GET.get('q')) & Q(departamento__empresa_id=self.request.user.userProfile.empresa_id))
    #     else:
    #         queryset = AtendimentosDepartamento.objects.all()
    #     return queryset

    @method_decorator(permission_required(['global_permissions.ver_tipos_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendimentosDepartamentoListView, self).dispatch(*args, **kwargs)

class AtendimentosDepartamentoCreateView(MyCreateViewAtendimentosDepartamento):
    template_name = 'atendimentos_departamento/templates/create_view_atendimentos_departamento.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendimentosDepartamentoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        print("teste")

        atendimentodepartamento = form.save(commit=False)
        atendimentodepartamento.nome = atendimentodepartamento.tipo_atendimento.descricao
        atendimentodepartamento.save()
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_tipos_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendimentosDepartamentoCreateView, self).dispatch(*args, **kwargs)

class AtendimentosDepartamentoUpdateView(MyUpdateViewAtendimentosDepartamento):
    template_name = 'atendimentos_departamento/templates/create_view_atendimentos_departamento.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendimentosDepartamentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        atendimentodepartamento = form.save(commit=False)
        atendimentodepartamento.nome = atendimentodepartamento.tipo_atendimento.descricao
        atendimentodepartamento.save()
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_tipos_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendimentosDepartamentoUpdateView, self).dispatch(*args, **kwargs)

@login_required()
def getTipoProfissionalPorIdTipoAtendimento(request, idTipoAtendimento):
    subs = {}
    tipo_atendimento = TipoAtendimento.objects.get(pk=idTipoAtendimento)

    subs['idProfissional'] = tipo_atendimento.tipo_profissional.pk
    return JsonResponse(subs)
