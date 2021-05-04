from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission, User, Group
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework.authtoken.models import Token

from core.models import Departamento,DepartamentoProfissional,Escala
from core.modulos.atendente.atendente import Atendente
from core.modulos.atendimento.atendimento import Atendimento
from core.modulos.escala.views_escala import mobile
from core.modulos.profissional.form_profissional import ProfissionalForm
from core.modulos.profissional.profissional import Profissional
from core.modulos.user_profile.user_profile import UserProfile, UserComum
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa, get_user_type


class MyGenericView(object):
    model = Profissional
    form_class = ProfissionalForm
    success_url = reverse_lazy('core:modulo:profissional:list_view')
    search_fields = []
    COLUMNS = [LabesProperty.NOME, LabesProperty.USUARIO, LabesProperty.DEPARTAMENTO]
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

    def get_queryset(self):
        usuario = get_user_type(self.request.user)

        if (self.request.GET.get('q')):
            queryset = Profissional.objects.filter((Q(userProfile__nome=self.request.GET.get('q')) | Q(userProfile__usuario__icontains=self.request.GET.get('q')) )& Q(departamentoprofissional__departamento__empresa_id=usuario.userProfile.departamento.empresa_id))
        else:
            queryset = Profissional.objects.filter(departamentoprofissional__departamento__empresa_id=usuario.userProfile.departamento.empresa_id)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    @method_decorator(permission_required(['global_permissions.ver_profissionais'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ProfissionalListView, self).dispatch(*args, **kwargs)

class ProfissionalCreateView(MyCreateViewProfissional):
    template_name = 'profissional/templates/create_view_profissional.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ProfissionalCreateView, self).form_invalid(form)

    def form_valid(self, form):

        # departamento_profissional.save()
        profissionalForm = form.save(commit=False)

        user = User.objects.create_user(
            first_name=self.request.POST.get('nome'),
            username=self.request.POST.get('usuario'),
            password='admin123admin',
            email=self.request.POST.get('email')
        )
        user.groups.add(Group.objects.get(name='Profissional').pk)  # Perfil do Profissional Padrão
        user.save()

        userComum = UserComum()
        userComum.save()
        userComum.user.groups.add(Group.objects.get(name='Profissional').pk)
        userComum.nome = self.request.POST.get('nome')
        userComum.usuario = self.request.POST.get('usuario')
        userComum.senha = 'admin123admin'
        userComum.user = user
        userComum.perfil_id = Group.objects.get(name='Profissional').pk  # Perfil do Profissional Padrão
        userComum.email = self.request.POST.get('email')
        userComum.save()
        profissionalForm.userComum = userComum

        # TODO - Veriricar a estratégia de senha

        Token.objects.get_or_create(user=user)

        user.get_group_permissions()

        profissionalForm.save()
        # Criar e popular os campos DepartamentoProfissional
        departamento_profissional = DepartamentoProfissional()
        departamento_profissional.departamento_id = self.request.POST.get('departamento')
        departamento_profissional.tipo_profissional_id = self.request.POST.get('tipo_profissional')
        departamento_profissional.profissional = profissionalForm
        departamento_profissional.save()
        self.request.session['save_model'] = 'true'

        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_profissionais'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ProfissionalCreateView, self).dispatch(*args, **kwargs)

class ProfissionalUpdateView(MyUpdateViewProfissional):
    template_name = 'profissional/templates/create_view_profissional.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ProfissionalUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        # solução abaixo está incompleta para atualizar grupo de usuário
        profissionalForm = form.save(commit=False)
        profissional = Profissional.objects.get(pk=self.object.pk)

        profissional.userComum.user.username =self.request.POST.get('usuario')
        profissional.userComum.usuario = self.request.POST.get('usuario')
        profissional.userComum.email =  self.request.POST.get('email')
        profissional.userComum.user.email = self.request.POST.get('email')
        profissional.userComum.user.first_name = self.request.POST.get('nome')
        profissional.userComum.nome = self.request.POST.get('nome')


        profissional.userComum.user.save()
        profissional.userComum.save()
        profissional.save()
        Token.objects.get_or_create(user=profissional.userComum.user)
        """user = User.objects.get(pk=userProfile.pk)
        print(dir(userProfile))
        user.groups.add(userProfile.perfil_id)
        user.save()"""
        # Atualiza varlores do Departamento Profissional
        departamento_profissional = DepartamentoProfissional.objects.get(profissional_id=self.object.id)
        departamento_profissional.departamento_id =self.request.POST.get('departamento')
        departamento_profissional.tipo_profissional_id =self.request.POST.get('tipo_profissional')

        departamento_profissional.save()
        profissionalForm.userComum=profissional.userComum
        profissionalForm.save()
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_profissionais'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        dep_prof = DepartamentoProfissional.objects.get(profissional_id=self.get_object().pk)
        usuario = get_user_type(self.request.user)

        if usuario.userProfile.departamento.empresa ==  dep_prof.departamento.empresa:
            return super().dispatch(self.request, *args, **kwargs)
        else:
            return redirect('core:modulo:dashboard')


class ProfissionalEscalaUpdateView(MyUpdateViewProfissional):
    template_name = 'escala/templates/create_view_escala.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.object.pk)
        context['idProfissional'] = self.object.pk
        departamento = self.request.user.userProfile.departamento_id
        depatamentoProfissional = DepartamentoProfissional.objects.get(departamento_id=departamento,
                                                                       profissional_id=self.object.pk)
        escalas = Escala.objects.filter(departamentoProfissional_id=depatamentoProfissional.pk)
        intervalos = []
        for escala in escalas:
            intervalo = escala.escalaintervalo_set.filter(escala_id=escala.pk)
            atendimento_anterior = None
            for inter in intervalo:
                if inter.atendimento != None:
                    atendimento = Atendimento.objects.get(pk=inter.atendimento)
                    b = {'id': atendimento.pk,
                         'title': atendimento.paciente.nome.split(" ")[0],
                         'start': str(escala.dia) + "T" + str(inter.inicio),
                         'end': str(escala.dia) + "T" + atendimento.fim_atendimento.strftime("%H:%M"),
                         'className': "fc-danger",
                         'cliente': atendimento.paciente.nome.split(" ")[0],
                         'inicio': atendimento.inicio_atendimento.strftime("%Hh%M"),
                         'tipo_atendimento': atendimento.tipoAtendimento.nome,
                         'fim': atendimento.fim_atendimento.strftime("%Hh%M")
                         }
                    if (
                            inter.atendimento == atendimento_anterior):  # Verifica se é um atendimento em sequência de intervalos
                        continue

                    atendimento_anterior = inter.atendimento  # Armazena o primeiro e id de um atendimento em sequencia de intervalos
                else:
                    b = {'id': inter.pk,
                         'title': "Disponível",
                         'start': str(escala.dia) + "T" + str(inter.inicio),
                         'end': str(escala.dia) + "T" + str(inter.fim),
                         'description': inter.descricao,
                         'className': "fc-success"
                         }

                intervalos.append(b)

        context['intervalos'] = intervalos
        if mobile(self.request):
            is_mobile = True
        else:
            is_mobile = False
        print(is_mobile)
        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(ProfissionalEscalaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        print(self.request.POST)
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.ver_escalas_profissionais'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ProfissionalEscalaUpdateView, self).dispatch(*args, **kwargs)

@login_required()
def getDepartamentosPorIdEmpresa(request, idEmpresa):
    subs = {}
    departamentos = Departamento.objects.filter(empresa_id=idEmpresa)

    for dep in departamentos:
        subs[dep.id] = dep.nome
    return JsonResponse(subs)
