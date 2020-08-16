import calendar
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, TemplateView

from core.models import Escala, EscalaIntervalo, Profissional, Atendimento
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa


class MyGenericView(object):
    model = Escala
    search_fields = ['departamentoProfissional']
    COLUMNS = [LabesProperty.PROFISSIONAL]
    NAME_MODEL = Escala._meta.verbose_name
    NAME_MODEL_PLURAL = Escala._meta.verbose_name_plural

class MyUpdateViewMinhaEscala(MyGenericView, LoginRequiredMixin, MyLabls, TemplateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass



class MinhaEscalaUpdateView(MyUpdateViewMinhaEscala):
    template_name = 'escala/templates/create_view_escala.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.object.departamentoProfissional_id)
        profissional = Profissional.objects.get(pk=self.request.user.userProfissional.pk)
        context['idProfissional'] = profissional.pk
        escalas = Escala.objects.filter(departamentoProfissional__profissional=self.request.user.userProfissional.pk, dia__gte=datetime.now().date())
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
                         'tipo_atendimento': atendimento.tipoAtendimento.descricao,
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
        return context

    @method_decorator(permission_required(['global_permissions.ver_minha_escala'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(MinhaEscalaUpdateView, self).dispatch(*args, **kwargs)