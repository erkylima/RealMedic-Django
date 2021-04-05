from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework.authtoken.models import Token

from core.models import Atendente
from core.modulos.atendente.form_atendente import AtendenteForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa, get_user_type


class MyGenericView(object):
    model = Atendente
    form_class = AtendenteForm
    success_url = reverse_lazy('core:modulo:atendente:list_view')
    search_fields = ['nome', 'usuario']
    COLUMNS = [LabesProperty.NOME, LabesProperty.USUARIO, LabesProperty.DEPARTAMENTO]
    NAME_MODEL = Atendente._meta.verbose_name
    NAME_MODEL_PLURAL = Atendente._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:atendente:create_view')

class MyListViewAtendente(MyGenericView, LoginRequiredMixin,
                            MyListViewSearcheGeneric,
                            MyLabls,
                            ListView):
    allow_empty = True
    paginate_by = 10

    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'


class MyCreateViewAtendente(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewAtendente(MyGenericView, LoginRequiredMixin, ValidarEmpresa, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class AtendenteListView(MyListViewAtendente):
    template_name = 'atendente/templates/list_view_atendente.html'

    def get_queryset(self):
        usuario = get_user_type(self.request.user)

        if (self.request.GET.get('q')):
            queryset = Atendente.objects.filter(Q(userProfile__nome__icontains=self.request.GET.get('q')) & Q(userProfile__departamento__empresa_id=usuario.userProfile.departamento.empresa_id))
        else:
            queryset = Atendente.objects.filter(userProfile__departamento__empresa_id=usuario.userProfile.departamento.empresa_id)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    @method_decorator(permission_required(['global_permissions.ver_atendentes'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendenteListView, self).dispatch(*args, **kwargs)

class AtendenteCreateView(MyCreateViewAtendente):
    template_name = 'atendente/templates/create_view_atendente.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendenteCreateView, self).form_invalid(form)

    def form_valid(self, form):

        userProfile = form.save(commit=False)
        # TODO - Veriricar a estratégia de senha
        user = User.objects.create_user(
            username=userProfile.usuario,
            password='admin123admin',
        )
        user.groups.add(userProfile.perfil_id)
        user.save()
        Token.objects.get_or_create(user=user)
        userProfile.perfil_id = 4
        userProfile.user = user
        userProfile.save()
        atendente = Atendente()
        atendente.userProfile = userProfile
        atendente.save()
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_atendentes'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendenteCreateView, self).dispatch(*args, **kwargs)

class AtendenteUpdateView(MyUpdateViewAtendente):
    template_name = 'atendente/templates/create_view_atendente.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendenteUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_atendentes'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendenteUpdateView, self).dispatch(*args, **kwargs)