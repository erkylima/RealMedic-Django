from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Atendente
from core.modulos.atendente.form_atendente import AtendenteForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = Atendente
    form_class = AtendenteForm
    success_url = reverse_lazy('core:modulo:atendente:list_view')
    search_fields = ['nome', 'usuario']
    COLUMNS = [LabesProperty.NOME, LabesProperty.USUARIO, LabesProperty.PERFIL]
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


class MyUpdateViewAtendente(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class AtendenteListView(MyListViewAtendente):
    template_name = 'atendente/templates/list_view_atendente.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AtendenteCreateView(MyCreateViewAtendente):
    template_name = 'atendente/templates/create_view_atendente.html'

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
        # user.groups.add(userProfile.group)
        # user.save()
        userProfile.user = user
        userProfile.save()
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class AtendenteUpdateView(MyUpdateViewAtendente):
    template_name = 'atendente/templates/create_view_atendente.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendenteUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)