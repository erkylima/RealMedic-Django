from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import View

from core.models import Atendimento
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa, get_user_type
from profissional.modulos.meus_atendimentos.form_meus_atendimentos import MeusAtendimentosForm


class MyGenericView(object):
    model = Atendimento
    form_class = MeusAtendimentosForm
    success_url = reverse_lazy('profissional:modulo:meus_atendimentos:list_view')
    search_fields = ['paciente__nome', 'tipoAtendimento__descricao','departamentoProfissional__pk']
    COLUMNS = [LabesProperty.NOME, LabesProperty.ATENDIMENTO, LabesProperty.VALOR, LabesProperty.DATA]
    NAME_MODEL = Atendimento._meta.verbose_name
    NAME_MODEL_PLURAL = Atendimento._meta.verbose_name_plural
    # PAGE_CREATE_VIEW = reverse_lazy('profissional:modulo:meus_atendimentos:list_view')


class MyListViewMeusAtendimentos(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True

class MyDetailViewMeusAtendimentos(MyGenericView, LoginRequiredMixin, MyLabls, View):
    pass


class MyCreateViewMeusAtendimentos(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewMeusAtendimentos(MyGenericView, LoginRequiredMixin, ValidarEmpresa, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MeusAtendimentosListView(MyListViewMeusAtendimentos):
    template_name = 'meus_atendimentos/templates/list_view_meus_atendimentos.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def get_queryset(self):
        usuario = get_user_type(self.request.user)
        if(self.request.GET.get('q')):
            queryset = Atendimento.objects.filter((Q(paciente__nome__icontains=self.request.GET.get('q')) |
                                                   Q(tipoAtendimento__descricao__icontains=self.request.GET.get('q').upper()) |
                                                   Q(valor__contains=self.request.GET.get('q'))) &
                                                  Q(departamentoProfissional__profissional_id=usuario.pk)).order_by('intervalo__escala__dia', 'inicio_atendimento')
        else:
            queryset = Atendimento.objects.filter(Q(departamentoProfissional__profissional_id=usuario.pk)).order_by('-intervalo__escala__dia', 'inicio_atendimento')
            print(dir(queryset.first()))
        return queryset

    @method_decorator(permission_required(['global_permissions.ver_meus_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(MeusAtendimentosListView, self).dispatch(*args, **kwargs)


class MeusAtendimentosUpdateView(MyUpdateViewMeusAtendimentos):
    template_name = 'meus_atendimentos/templates/create_view_meus_atendimentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(MeusAtendimentosUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.ver_meus_pacientes'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(MeusAtendimentosUpdateView, self).dispatch(*args, **kwargs)