import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from core.modulos.atendimento.atendimento import Atendimento
from core.modulos.paciente.paciente import PacienteDepartamentoProfissional
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

        start = datetime.date(2020, mes_atual -1 , 31)

        end = datetime.date(2020, 8, 31)
        new_end = end + datetime.timedelta(days=1)

        atendimentos_profissional_julho = Atendimento.objects.filter(intervalo__escala__dia__month=7).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)
        atendimentos_profissional_agosto = Atendimento.objects.filter(intervalo__escala__dia__month=8).filter(
            departamentoProfissional__profissional_id=self.request.user.userProfissional.pk).filter(pago=True)

        pacientes_profissional_mes = PacienteDepartamentoProfissional.objects.filter(data_cadastro__range=[start,end], departamentoProfissional__profissional_id=self.request.user.userProfissional.pk)
        qnt_clientes_profissional_mes = len(pacientes_profissional_mes)
        qnt_atendimentos_profissional_julho = 0
        valor_atendimentos_profissional_julho = 0

        for key, atendimento in enumerate(atendimentos_profissional_julho):
            valor_atendimentos_profissional_julho += atendimento.valor
            qnt_atendimentos_profissional_julho = key+1

        qnt_atendimentos_profissional_agosto = 0
        valor_atendimentos_profissional_agosto = 0
        for key, atendimento in enumerate(atendimentos_profissional_agosto):
            valor_atendimentos_profissional_agosto += atendimento.valor
            qnt_atendimentos_profissional_agosto = key + 1


        context['qnt_atendimentos_julho'] = qnt_atendimentos_profissional_julho
        context['atendimentos_julho'] = valor_atendimentos_profissional_julho
        context['qnt_atendimentos_agosto'] = qnt_atendimentos_profissional_agosto
        context['atendimentos_agosto'] = valor_atendimentos_profissional_agosto
        context['qnt_clientes_profissional_mes'] = qnt_clientes_profissional_mes
        total = valor_atendimentos_profissional_julho + valor_atendimentos_profissional_agosto
        context['total'] = total
        return context

    @method_decorator(permission_required(['global_permissions.ver_painel_profissional'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(RelatorioView, self).dispatch(*args, **kwargs)