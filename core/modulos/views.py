import datetime

from dateutil.relativedelta import relativedelta

from django.contrib import auth
from django.contrib.auth import user_logged_out
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Q
from django.db.models.expressions import RawSQL
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.core import serializers

from core.models import Atendimento, Cliente
from core.modulos.atendente.atendente import Atendente
from core.modulos.paciente.paciente import Paciente
from core.modulos.profissional.profissional import Profissional, DepartamentoProfissional
from core.util.util_manager import MyLabls, get_user_type, get_data_por_idade


class DashBoard(MyLabls, LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        print('get_context_data')
        context = super().get_context_data(**kwargs)
        dados = {}

        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        usuario = get_user_type(self.request.user)
        pacientes_10 = Paciente.objects.filter(
            Q(departamento__empresa_id=usuario.userProfile.departamento.empresa_id,
              data_nascimento__range=[get_data_por_idade(10), get_data_por_idade(0)])).count()
        pacientes_20 = Paciente.objects.filter(
            Q(departamento__empresa_id=usuario.userProfile.departamento.empresa_id,
              data_nascimento__range=[get_data_por_idade(20), get_data_por_idade(11)])).count()
        pacientes_30 = Paciente.objects.filter(
            Q(departamento__empresa_id=usuario.userProfile.departamento.empresa_id,
              data_nascimento__range=[get_data_por_idade(30), get_data_por_idade(21)])).count()
        pacientes_40 = Paciente.objects.filter(
            Q(departamento__empresa_id=usuario.userProfile.departamento.empresa_id,
              data_nascimento__range=[get_data_por_idade(40), get_data_por_idade(31)])).count()
        pacientes_50 = Paciente.objects.filter(
            Q(departamento__empresa_id=usuario.userProfile.departamento.empresa_id,
              data_nascimento__range=[get_data_por_idade(50), get_data_por_idade(41)])).count()
        pacientes_60 = Paciente.objects.filter(
            Q(departamento__empresa_id=usuario.userProfile.departamento.empresa_id,
              data_nascimento__range=[get_data_por_idade(60), get_data_por_idade(51)])).count()
        pacientes_70 = Paciente.objects.filter(
            Q(departamento__empresa_id=usuario.userProfile.departamento.empresa_id,
              data_nascimento__range=[get_data_por_idade(70), get_data_por_idade(61)])).count()
        pacientes_80 = Paciente.objects.filter(
            Q(departamento__empresa_id=usuario.userProfile.departamento.empresa_id,
              data_nascimento__range=[get_data_por_idade(120), get_data_por_idade(80)])).count()

        corpo_clinico = DepartamentoProfissional.objects.filter(
            departamento_id=usuario.userProfile.departamento_id)
        pacientes = Paciente.objects.filter(departamento_id=usuario.userProfile.departamento_id)
        print(usuario.userProfile.departamento.empresa)

        atendimentos_janeiro = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=1)
        atendimentos_fevereiro = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=2)
        atendimentos_marco = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=3)
        atendimentos_abril = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=4)
        atendimentos_maio = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=5)
        atendimentos_junho = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=6)
        atendimentos_julho = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=7)
        atendimentos_agosto = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=8)
        atendimentos_setembro = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=9)
        atendimentos_outubro = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=10)
        atendimentos_novembro = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=11)
        atendimentos_dezembro = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id).filter(intervalo__escala__dia__month=12)

        atendimentos = Atendimento.objects.filter(
            departamentoProfissional__departamento_id=usuario.userProfile.departamento_id)

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

        context['atendimentos_janeiro'] = atendimentos_janeiro.aggregate(sum=Sum('valor'))
        context['atendimentos_fevereiro'] = atendimentos_fevereiro.aggregate(sum=Sum('valor'))
        context['atendimentos_marco'] = atendimentos_marco.aggregate(sum=Sum('valor'))
        context['atendimentos_abril'] = atendimentos_abril.aggregate(sum=Sum('valor'))
        context['atendimentos_maio'] = atendimentos_maio.aggregate(sum=Sum('valor'))
        context['atendimentos_junho'] = atendimentos_junho.aggregate(sum=Sum('valor'))
        context['atendimentos_julho'] = atendimentos_julho.aggregate(sum=Sum('valor'))
        context['atendimentos_agosto'] = atendimentos_agosto.aggregate(sum=Sum('valor'))
        context['atendimentos_setembro'] = atendimentos_setembro.aggregate(sum=Sum('valor'))
        context['atendimentos_outubro'] = atendimentos_outubro.aggregate(sum=Sum('valor'))
        context['atendimentos_novembro'] = atendimentos_novembro.aggregate(sum=Sum('valor'))
        context['atendimentos_dezembro'] = atendimentos_dezembro.aggregate(sum=Sum('valor'))

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
