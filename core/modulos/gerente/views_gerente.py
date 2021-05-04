from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework.authtoken.models import Token

from core.modulos.gerente.form_gerente import GerenteForm
from core.modulos.gerente.gerente import Gerente
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa


class MyGenericView(object):
    model = Gerente
    form_class = GerenteForm
    success_url = reverse_lazy('core:modulo:gerente:list_view')
    search_fields = ['nome', 'usuario']
    COLUMNS = [LabesProperty.NOME, LabesProperty.USUARIO, LabesProperty.PERFIL]
    NAME_MODEL = Gerente._meta.verbose_name
    NAME_MODEL_PLURAL = Gerente._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:gerente:create_view')


class MyListViewGerente(MyGenericView,LoginRequiredMixin,
                            MyListViewSearcheGeneric,
                            MyLabls,
                            ListView):
    allow_empty = True

    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'


class MyCreateViewGerente(MyGenericView,LoginRequiredMixin, MyLabls, CreateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewGerente(MyGenericView,LoginRequiredMixin, ValidarEmpresa, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class GerenteListView(MyListViewGerente):
    template_name = 'gerente/templates/list_view_gerente.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    @method_decorator(permission_required(['global_permissions.ver_gerente'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(GerenteListView, self).dispatch(*args, **kwargs)


class GerenteCreateView(MyCreateViewGerente):
    template_name = 'gerente/templates/create_view_gerente.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(GerenteCreateView, self).form_invalid(form)

    def form_valid(self, form):
        gerente = form.save(commit=False)
        # TODO - Veriricar a estratégia de senha
        user = User.objects.create_user(
            username=gerente.usuario,
            password='admin123admin',
        )
        user.groups.add(gerente.perfil_id)
        user.save()
        gerente.userProfile.user = user
        gerente.save()
        Token.objects.get_or_create(user=user)

        self.request.session['save_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_gerente'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(GerenteCreateView, self).dispatch(*args, **kwargs)

class GerenteUpdateView(MyUpdateViewGerente):
    template_name = 'gerente/templates/create_view_gerente.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(GerenteUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        gerente = form.save(commit=False)
        user = gerente.userProfile.user
        Token.objects.get_or_create(user=user)

        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_gerente'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(GerenteUpdateView, self).dispatch(*args, **kwargs)