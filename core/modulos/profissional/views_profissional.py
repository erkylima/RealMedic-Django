from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.models import Profissional,Departamento,DepartamentoProfissional
from core.modulos.profissional.form_profissional import ProfissionalForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = Profissional
    form_class = ProfissionalForm
    success_url = reverse_lazy('core:modulo:profissional:list_view')
    search_fields = ['nome', 'usuario']
    COLUMNS = [LabesProperty.NOME, LabesProperty.USUARIO, LabesProperty.PERFIL]
    NAME_MODEL = Profissional._meta.verbose_name
    NAME_MODEL_PLURAL = Profissional._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:profissional:create_view')


class MyListViewProfissional(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True


class MyCreateViewProfissional(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewProfissional(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class ProfissionalListView(MyListViewProfissional):
    template_name = 'profissional/templates/list_view_profissional.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class ProfissionalCreateView(MyCreateViewProfissional):
    template_name = 'profissional/templates/create_view_profissional.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ProfissionalCreateView, self).form_invalid(form)

    def form_valid(self, form):

        # departamento_profissional.save()
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
        departamento_profissional = DepartamentoProfissional()
        departamento_profissional.departamento = Departamento.objects.get(pk=self.request.POST.get('departamento'))
        # type(Departamento.objects.get(pk=self.request.POST.get('departamento')))
        departamento_profissional.profissional = userProfile
        departamento_profissional.save()
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class ProfissionalUpdateView(MyUpdateViewProfissional):
    template_name = 'profissional/templates/create_view_profissional.html'

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ProfissionalUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)


@login_required()
def getDepartamentosPorIdEmpresa(request, idEmpresa):
    subs = {}
    departamentos = Departamento.objects.filter(empresa_id=idEmpresa)

    for dep in departamentos:
        subs[dep.id] = dep.nome
    return JsonResponse(subs)
