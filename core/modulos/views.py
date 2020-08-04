import datetime

from django.contrib import auth
from django.contrib.auth import user_logged_out
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.core import serializers

from core.models import Atendimento, Cliente
from core.modulos.paciente.paciente import Paciente
from core.modulos.profissional.profissional import Profissional, DepartamentoProfissional
from core.util.util_manager import MyLabls


class DashBoard(MyLabls, LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        print('get_context_data')
        context = super().get_context_data(**kwargs)
        atendimentos = Atendimento.objects.all()
        dados = {}
        yesterday = datetime.date.today() - datetime.timedelta(days=1)

        clientes = Cliente.objects.filter(data_cadastro__gt=yesterday)
        tclientes = Cliente.objects.all()

        try:
            pacientes_10 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userAtendente.departamento.empresa_id, idade__range=[0, 10])).count()
            pacientes_20 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userAtendente.departamento.empresa_id, idade__range=[11, 20])).count()
            pacientes_30 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userAtendente.departamento.empresa_id, idade__range=[21, 30])).count()
            pacientes_40 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userAtendente.departamento.empresa_id, idade__range=[31, 40])).count()
            pacientes_50 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userAtendente.departamento.empresa_id, idade__range=[41, 50])).count()
            pacientes_60 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userAtendente.departamento.empresa_id, idade__range=[51, 60])).count()
            pacientes_70 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userAtendente.departamento.empresa_id, idade__range=[61, 79])).count()
            pacientes_80 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userAtendente.departamento.empresa_id, idade__range=[80, 100])).count()

            corpo_clinico = DepartamentoProfissional.objects.filter(departamento_id=self.request.user.userAtendente.departamento_id)
        except:
            pacientes_10 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userProfile.departamento.empresa_id,
                  idade__range=[0, 10])).count()
            pacientes_20 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userProfile.departamento.empresa_id,
                  idade__range=[11, 20])).count()
            pacientes_30 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userProfile.departamento.empresa_id,
                  idade__range=[21, 30])).count()
            pacientes_40 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userProfile.departamento.empresa_id,
                  idade__range=[31, 40])).count()
            pacientes_50 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userProfile.departamento.empresa_id,
                  idade__range=[41, 50])).count()
            pacientes_60 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userProfile.departamento.empresa_id,
                  idade__range=[51, 60])).count()
            pacientes_70 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userProfile.departamento.empresa_id,
                  idade__range=[61, 79])).count()
            pacientes_80 = Paciente.objects.filter(
                Q(departamento__empresa_id=self.request.user.userProfile.departamento.empresa_id,
                  idade__range=[80, 100])).count()

            corpo_clinico = DepartamentoProfissional.objects.filter(
                departamento_id=self.request.user.userProfile.departamento_id)
        context['pacientes_10'] = pacientes_10
        context['pacientes_20'] = pacientes_20
        context['pacientes_30'] = pacientes_30
        context['pacientes_40'] = pacientes_40
        context['pacientes_50'] = pacientes_50
        context['pacientes_60'] = pacientes_60
        context['pacientes_70'] = pacientes_70
        context['pacientes_80'] = pacientes_80
        context['corpo_clinico'] = corpo_clinico



        context['clientes'] = clientes
        context['tclientes'] = tclientes
        context['total'] = atendimentos.aggregate(sum= Sum('valor'))
        # print(atendimentos.aggregate(sum= Sum('valor')))
        context['atendimentos'] = atendimentos

        # print(dir(self.request.user.perfil_id))

        context.update(dados)

        return context

@login_required
def logout_view(request):
    user = getattr(request, 'user', None)
    user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)


    from django.contrib.auth.models import AnonymousUser
    request.user = AnonymousUser()
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('core:login'))