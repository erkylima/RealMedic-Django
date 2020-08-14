from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from core.models import Prontuario
from profissional.modulos.prontuario.form_prontuario import ProntuarioForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa


class MyGenericView(object):
    model = Prontuario
    form_class = ProntuarioForm
    success_url = reverse_lazy('profissional:modulo:meus_pacientes:list_view')
    search_fields = ['nome']
    COLUMNS = [LabesProperty.NOME]
    NAME_MODEL = Prontuario._meta.verbose_name
    NAME_MODEL_PLURAL = Prontuario._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:prontuario:create_view')

class MyCreateViewProntuario(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewProntuario(MyGenericView, LoginRequiredMixin, ValidarEmpresa, MyLabls, UpdateView):
    permission_required = 'global_permissions.ver_prontuario'
    # permission_denied_message = 'Permission Denied'
    pass

class ProntuarioCreateView(MyCreateViewProntuario):
    template_name = 'prontuario/templates/create_view_prontuario.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))

        return super(ProntuarioCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        prontuario = form.save(commit=False)

        form.save(commit=False)
        return super().form_valid(form)


class ProntuarioUpdateView(MyUpdateViewProntuario):
    template_name = 'prontuario/templates/create_view_prontuario.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ProntuarioUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        prontuario = form.save(commit=False)

        return super().form_valid(form)

