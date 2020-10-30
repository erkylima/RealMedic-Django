import calendar
import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Q
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from core.modulos.atendimento.atendimento import Atendimento
from core.modulos.paciente.paciente import PacienteDepartamentoProfissional, Paciente
from core.modulos.profissional.profissional import DepartamentoProfissional
from core.util.util_manager import MyLabls


class MyViewRelatorio(LoginRequiredMixin, MyLabls, TemplateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass



class RelatorioView(MyViewRelatorio):
    template_name = 'relatorio/templates/detalhes_relatorio_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mes_atual = int(datetime.date.today().month)

        print(mes_atual-1)
        start = datetime.date(2020, mes_atual - 1, calendar.monthrange(2020, mes_atual - 1)[1])

        end = datetime.date(2020, 8, 31)
        new_end = end + datetime.timedelta(days=1)

        atendimentos_profissional_janeiro = Atendimento.objects.filter(intervalo__escala__dia__month=1).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_fevereiro = Atendimento.objects.filter(intervalo__escala__dia__month=2).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_marco = Atendimento.objects.filter(intervalo__escala__dia__month=3).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_abril = Atendimento.objects.filter(intervalo__escala__dia__month=4).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_maio = Atendimento.objects.filter(intervalo__escala__dia__month=5).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_junho = Atendimento.objects.filter(intervalo__escala__dia__month=6).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_julho = Atendimento.objects.filter(intervalo__escala__dia__month=7).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_agosto = Atendimento.objects.filter(intervalo__escala__dia__month=8).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_setembro = Atendimento.objects.filter(intervalo__escala__dia__month=9).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_outubro = Atendimento.objects.filter(intervalo__escala__dia__month=10).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_novembro = Atendimento.objects.filter(intervalo__escala__dia__month=11).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        atendimentos_profissional_dezembro = Atendimento.objects.filter(intervalo__escala__dia__month=12).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        # JANEIRO
        qnt_atendimentos_profissional_janeiro = 0
        valor_atendimentos_profissional_janeiro = 0

        for key, atendimento in enumerate(atendimentos_profissional_janeiro):
            valor_atendimentos_profissional_janeiro += atendimento.valor
            qnt_atendimentos_profissional_janeiro = key + 1

        context['qnt_atendimentos_janeiro'] = qnt_atendimentos_profissional_janeiro
        context['atendimentos_janeiro'] = valor_atendimentos_profissional_janeiro

        # FEVEREIRO
        qnt_atendimentos_profissional_fevereiro = 0
        valor_atendimentos_profissional_fevereiro = 0

        for key, atendimento in enumerate(atendimentos_profissional_fevereiro):
            valor_atendimentos_profissional_fevereiro += atendimento.valor
            qnt_atendimentos_profissional_fevereiro = key + 1

        context['qnt_atendimentos_fevereiro'] = qnt_atendimentos_profissional_fevereiro
        context['atendimentos_fevereiro'] = valor_atendimentos_profissional_fevereiro

        # MARCO
        qnt_atendimentos_profissional_marco = 0
        valor_atendimentos_profissional_marco = 0

        for key, atendimento in enumerate(atendimentos_profissional_marco):
            valor_atendimentos_profissional_marco += atendimento.valor
            qnt_atendimentos_profissional_marco = key + 1

        context['qnt_atendimentos_marco'] = qnt_atendimentos_profissional_marco
        context['atendimentos_marco'] = valor_atendimentos_profissional_marco

        # ABRIL
        qnt_atendimentos_profissional_abril = 0
        valor_atendimentos_profissional_abril = 0

        for key, atendimento in enumerate(atendimentos_profissional_abril):
            valor_atendimentos_profissional_abril += atendimento.valor
            qnt_atendimentos_profissional_abril = key + 1

        context['qnt_atendimentos_abril'] = qnt_atendimentos_profissional_abril
        context['atendimentos_abril'] = valor_atendimentos_profissional_abril

        # MAIO
        qnt_atendimentos_profissional_maio = 0
        valor_atendimentos_profissional_maio = 0

        for key, atendimento in enumerate(atendimentos_profissional_maio):
            valor_atendimentos_profissional_maio += atendimento.valor
            qnt_atendimentos_profissional_maio = key + 1

        context['qnt_atendimentos_maio'] = qnt_atendimentos_profissional_maio
        context['atendimentos_maio'] = valor_atendimentos_profissional_maio

        # JUNHO
        qnt_atendimentos_profissional_junho = 0
        valor_atendimentos_profissional_junho = 0

        for key, atendimento in enumerate(atendimentos_profissional_junho):
            valor_atendimentos_profissional_junho += atendimento.valor
            qnt_atendimentos_profissional_junho = key + 1

        context['qnt_atendimentos_junho'] = qnt_atendimentos_profissional_junho
        context['atendimentos_junho'] = valor_atendimentos_profissional_junho

        # JULHO
        qnt_atendimentos_profissional_julho = 0
        valor_atendimentos_profissional_julho = 0

        for key, atendimento in enumerate(atendimentos_profissional_julho):
            valor_atendimentos_profissional_julho += atendimento.valor
            qnt_atendimentos_profissional_julho = key + 1

        context['qnt_atendimentos_julho'] = qnt_atendimentos_profissional_julho
        context['atendimentos_julho'] = valor_atendimentos_profissional_julho

        # AGOSTO
        qnt_atendimentos_profissional_agosto = 0
        valor_atendimentos_profissional_agosto = 0
        for key, atendimento in enumerate(atendimentos_profissional_agosto):
            valor_atendimentos_profissional_agosto += atendimento.valor
            qnt_atendimentos_profissional_agosto = key + 1

        context['qnt_atendimentos_agosto'] = qnt_atendimentos_profissional_agosto
        context['atendimentos_agosto'] = valor_atendimentos_profissional_agosto

        # SETEMBRO
        qnt_atendimentos_profissional_setembro = 0
        valor_atendimentos_profissional_setembro = 0
        for key, atendimento in enumerate(atendimentos_profissional_setembro):
            valor_atendimentos_profissional_setembro += atendimento.valor
            qnt_atendimentos_profissional_setembro = key + 1
        context['qnt_atendimentos_setembro'] = qnt_atendimentos_profissional_setembro
        context['atendimentos_setembro'] = valor_atendimentos_profissional_setembro

        # OUTUBRO
        qnt_atendimentos_profissional_outubro = 0
        valor_atendimentos_profissional_outubro = 0
        for key, atendimento in enumerate(atendimentos_profissional_outubro):
            valor_atendimentos_profissional_outubro += atendimento.valor
            qnt_atendimentos_profissional_outubro = key + 1
        context['qnt_atendimentos_outubro'] = qnt_atendimentos_profissional_outubro
        context['atendimentos_outubro'] = valor_atendimentos_profissional_outubro

        # NOVEMBRO
        qnt_atendimentos_profissional_novembro = 0
        valor_atendimentos_profissional_novembro = 0
        for key, atendimento in enumerate(atendimentos_profissional_novembro):
            valor_atendimentos_profissional_novembro += atendimento.valor
            qnt_atendimentos_profissional_novembro = key + 1
        context['qnt_atendimentos_novembro'] = qnt_atendimentos_profissional_novembro
        context['atendimentos_novembro'] = valor_atendimentos_profissional_novembro

        # DEZEMBRO
        qnt_atendimentos_profissional_dezembro = 0
        valor_atendimentos_profissional_dezembro = 0
        for key, atendimento in enumerate(atendimentos_profissional_dezembro):
            valor_atendimentos_profissional_dezembro += atendimento.valor
            qnt_atendimentos_profissional_dezembro = key + 1
        context['qnt_atendimentos_dezembro'] = qnt_atendimentos_profissional_dezembro
        context['atendimentos_dezembro'] = valor_atendimentos_profissional_dezembro

        # CLIENTES DO MÊS CORRENTE
        pacientes_profissional_mes = PacienteDepartamentoProfissional.objects.filter(data_cadastro__range=[start, end],
                                                                                     departamentoProfissional__profissional_id=self.request.user.userProfissional.pk)
        qnt_clientes_profissional_mes = len(pacientes_profissional_mes)

        context['qnt_clientes_profissional_mes'] = qnt_clientes_profissional_mes

        qnt_mes_atual = Atendimento.objects.filter(intervalo__escala__dia__month=mes_atual).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        total = valor_atendimentos_profissional_janeiro + valor_atendimentos_profissional_fevereiro + valor_atendimentos_profissional_marco + valor_atendimentos_profissional_abril + valor_atendimentos_profissional_maio + valor_atendimentos_profissional_junho + valor_atendimentos_profissional_julho + valor_atendimentos_profissional_agosto + valor_atendimentos_profissional_setembro + valor_atendimentos_profissional_outubro + valor_atendimentos_profissional_novembro + valor_atendimentos_profissional_dezembro

        context['qnt_mes_atual'] = qnt_mes_atual.count()
        context['total'] = total

        dep_prof = DepartamentoProfissional.objects.get(profissional_id=self.request.user.userProfissional.pk)
        pacientes_10 = PacienteDepartamentoProfissional.objects.filter(
            Q(departamentoProfissional__departamento_id=dep_prof.departamento_id, departamentoProfissional__profissional_id=self.request.user.userProfissional.pk,
              paciente__idade__range=[0, 10])).count()
        pacientes_20 = PacienteDepartamentoProfissional.objects.filter(
            Q(departamentoProfissional__departamento_id=dep_prof.departamento_id, departamentoProfissional__profissional_id=self.request.user.userProfissional.pk,
              paciente__idade__range=[11, 20])).count()
        pacientes_30 = PacienteDepartamentoProfissional.objects.filter(
            Q(departamentoProfissional__departamento_id=dep_prof.departamento_id, departamentoProfissional__profissional_id=self.request.user.userProfissional.pk,
              paciente__idade__range=[21, 30])).count()
        pacientes_40 = PacienteDepartamentoProfissional.objects.filter(
            Q(departamentoProfissional__departamento_id=dep_prof.departamento_id, departamentoProfissional__profissional_id=self.request.user.userProfissional.pk,
              paciente__idade__range=[31, 40])).count()
        pacientes_50 = PacienteDepartamentoProfissional.objects.filter(
            Q(departamentoProfissional__departamento_id=dep_prof.departamento_id, departamentoProfissional__profissional_id=self.request.user.userProfissional.pk,
              paciente__idade__range=[41, 50])).count()
        pacientes_60 = PacienteDepartamentoProfissional.objects.filter(
            Q(departamentoProfissional__departamento_id=dep_prof.departamento_id, departamentoProfissional__profissional_id=self.request.user.userProfissional.pk,
              paciente__idade__range=[51, 60])).count()
        pacientes_70 = PacienteDepartamentoProfissional.objects.filter(
            Q(departamentoProfissional__departamento_id=dep_prof.departamento_id, departamentoProfissional__profissional_id=self.request.user.userProfissional.pk,
              paciente__idade__range=[61, 79])).count()
        pacientes_80 = PacienteDepartamentoProfissional.objects.filter(
            Q(departamentoProfissional__departamento_id=dep_prof.departamento_id, departamentoProfissional__profissional_id=self.request.user.userProfissional.pk,
              paciente__idade__range=[80, 100])).count()


        context['pacientes_10'] = pacientes_10
        context['pacientes_20'] = pacientes_20
        context['pacientes_30'] = pacientes_30
        context['pacientes_40'] = pacientes_40
        context['pacientes_50'] = pacientes_50
        context['pacientes_60'] = pacientes_60
        context['pacientes_70'] = pacientes_70
        context['pacientes_80'] = pacientes_80

        return context

@method_decorator(permission_required(['global_permissions.ver_painel_profissional'], raise_exception=True))
def dispatch(self, *args, **kwargs):
    return super(RelatorioView, self).dispatch(*args, **kwargs)