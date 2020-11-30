import datetime

from django.contrib import auth
from django.contrib.auth import user_logged_out
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.core import serializers

from core.models import Atendimento, Cliente
from core.modulos.atendente.atendente import Atendente
from core.modulos.paciente.paciente import Paciente
from core.modulos.profissional.profissional import Profissional, DepartamentoProfissional
from core.modulos.user_profile.user_profile import UserProfile
from core.util.util_manager import MyLabls, get_user_type


class DashBoard(MyLabls, LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        print('get_context_data')
        context = super().get_context_data(**kwargs)
        dados = {}
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        usuario = get_user_type(self.request.user)
        if isinstance(usuario,Atendente):
            pacientes_10 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.departamento.empresa_id,
                  idade__range=[0, 10])).count()
            pacientes_20 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.departamento.empresa_id,
                  idade__range=[11, 20])).count()
            pacientes_30 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.departamento.empresa_id,
                  idade__range=[21, 30])).count()
            pacientes_40 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.departamento.empresa_id,
                  idade__range=[31, 40])).count()
            pacientes_50 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.departamento.empresa_id,
                  idade__range=[41, 50])).count()
            pacientes_60 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.departamento.empresa_id,
                  idade__range=[51, 60])).count()
            pacientes_70 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.departamento.empresa_id,
                  idade__range=[61, 79])).count()
            pacientes_80 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.departamento.empresa_id,
                  idade__range=[80, 100])).count()

            corpo_clinico = DepartamentoProfissional.objects.filter(
                departamento_id=usuario.departamento_id)
            pacientes = Paciente.objects.filter(departamento_id=usuario.departamento_id)

            atendimentos = Atendimento.objects.filter(
                departamentoProfissional__departamento_id=usuario.departamento_id)
        elif isinstance(usuario, UserProfile):
            pacientes_10 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.empresa_id,
                  idade__range=[0, 10])).count()
            pacientes_20 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.empresa_id,
                  idade__range=[11, 20])).count()
            pacientes_30 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.empresa_id,
                  idade__range=[21, 30])).count()
            pacientes_40 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.empresa_id,
                  idade__range=[31, 40])).count()
            pacientes_50 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.empresa_id,
                  idade__range=[41, 50])).count()
            pacientes_60 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.empresa_id,
                  idade__range=[51, 60])).count()
            pacientes_70 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.empresa_id,
                  idade__range=[61, 79])).count()
            pacientes_80 = Paciente.objects.filter(
                Q(departamento__empresa_id=usuario.empresa_id,
                  idade__range=[80, 100])).count()
            corpo_clinico = DepartamentoProfissional.objects.filter(
                departamento__empresa_id=usuario.empresa_id)
            pacientes = Paciente.objects.filter(departamento__empresa_id=usuario.empresa_id)
            atendimentos = Atendimento.objects.filter(
                departamentoProfissional__departamento__empresa_id=usuario.empresa_id)
        else:
            dep_prof = DepartamentoProfissional.objects.get(profissional_id=usuario.pk)
            pacientes_10 = Paciente.objects.filter(
                Q(departamento_id=dep_prof.departamento_id,
                  idade__range=[0, 10])).count()
            pacientes_20 = Paciente.objects.filter(
                Q(departamento_id=dep_prof.departamento_id,
                  idade__range=[11, 20])).count()
            pacientes_30 = Paciente.objects.filter(
                Q(departamento_id=dep_prof.departamento_id,
                  idade__range=[21, 30])).count()
            pacientes_40 = Paciente.objects.filter(
                Q(departamento_id=dep_prof.departamento_id,
                  idade__range=[31, 40])).count()
            pacientes_50 = Paciente.objects.filter(
                Q(departamento_id=dep_prof.departamento_id,
                  idade__range=[41, 50])).count()
            pacientes_60 = Paciente.objects.filter(
                Q(departamento_id=dep_prof.departamento_id,
                  idade__range=[51, 60])).count()
            pacientes_70 = Paciente.objects.filter(
                Q(departamento_id=dep_prof.departamento_id,
                  idade__range=[61, 79])).count()
            pacientes_80 = Paciente.objects.filter(
                Q(departamento_id=dep_prof.departamento_id,
                  idade__range=[80, 100])).count()
            corpo_clinico = DepartamentoProfissional.objects.filter(
                departamento_id=dep_prof.departamento_id)
            pacientes = Paciente.objects.filter(departamento_id=dep_prof.departamento_id)
            atendimentos = Atendimento.objects.filter(
                departamentoProfissional__departamento_id=dep_prof.departamento_id)
        context['pacientes_10'] = pacientes_10
        context['pacientes_20'] = pacientes_20
        context['pacientes_30'] = pacientes_30
        context['pacientes_40'] = pacientes_40
        context['pacientes_50'] = pacientes_50
        context['pacientes_60'] = pacientes_60
        context['pacientes_70'] = pacientes_70
        context['pacientes_80'] = pacientes_80
        context['corpo_clinico'] = corpo_clinico

        context['pacientes'] = pacientes
        context['total'] = atendimentos.aggregate(sum=Sum('valor'))

        context['atendimentos'] = atendimentos


        context.update(dados)

        return context

    @method_decorator(permission_required(['global_permissions.ver_painel_geral'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(DashBoard, self).dispatch(*args, **kwargs)


@login_required
def logout_view(request):
    user = getattr(request, 'user', None)
    user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    from django.contrib.auth.models import AnonymousUser
    request.user = AnonymousUser()
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('core:login'))
