from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Cliente
from core.modulos.cliente.form_cliente import ClienteForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('core:modulo:cliente:list_view')
    search_fields = ['nome', 'usuario']
    COLUMNS = [LabesProperty.NOME, LabesProperty.USUARIO, LabesProperty.PERFIL]
    NAME_MODEL = Cliente._meta.verbose_name
    NAME_MODEL_PLURAL = Cliente._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:cliente:create_view')

class MyListViewCliente(MyGenericView, LoginRequiredMixin,
                            MyListViewSearcheGeneric,
                            MyLabls,
                            ListView):
    allow_empty = True
    paginate_by = 10

    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'


class MyCreateViewCliente(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewCliente(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class ClienteListView(MyListViewCliente):
    template_name = 'cliente/templates/list_view_cliente.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    @method_decorator(permission_required(['global_permissions.ver_clientes'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ClienteListView, self).dispatch(*args, **kwargs)

class ClienteCreateView(MyCreateViewCliente):
    template_name = 'cliente/templates/create_view_cliente.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ClienteCreateView, self).form_invalid(form)

    def form_valid(self, form):

        userProfile = form.save(commit=False)
        # TODO - Veriricar a estratégia de senha
        user = User.objects.create_user(
            username=userProfile.usuario,
            password='admin123admin',
        )
        user.groups.add(userProfile.perfil_id)
        user.save()
        userProfile.user = user
        userProfile.save()
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class ClienteUpdateView(MyUpdateViewCliente):
    template_name = 'cliente/templates/create_view_cliente.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ClienteUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)
