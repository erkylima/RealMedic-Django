from datetime import datetime, timedelta
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import View

from core.models import Atendimento, DepartamentoProfissional, Profissional, Escala, Paciente, EscalaIntervalo
from core.modulos.atendimento.form_atendimento import AtendimentoForm
from core.modulos.departamento.departamento import Departamento
from core.modulos.paciente.paciente import PacienteDepartamentoProfissional
from core.modulos.prontuario.prontuario import Prontuario
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls, ValidarEmpresa


class MyGenericView(object):
    model = DepartamentoProfissional
    form_class = AtendimentoForm
    success_url = reverse_lazy('core:modulo:atendimento:list_view')
    search_fields = ['profissional__nome', 'tipo_profissional__descricao']
    COLUMNS = [LabesProperty.NOME, LabesProperty.DOCUMENTO]
    NAME_MODEL = Atendimento._meta.verbose_name
    NAME_MODEL_PLURAL = Atendimento._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:atendimento:create_view')


class MyListViewAtendimento(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True

class MyDetailViewAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, View):
    pass

class MyCreateViewAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewAtendimento(MyGenericView, LoginRequiredMixin, ValidarEmpresa, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass

class AtendimentoDetailView(MyDetailViewAtendimento):
    template_name = 'atendimento/templates/list_view_atendimento.html'


class AtendimentoListView(MyListViewAtendimento):
    template_name = 'atendimento/templates/list_view_atendimento.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        try:
            context['departamentoprofissional_list'] = DepartamentoProfissional.objects.filter(departamento_id=self.request.user.userAtendente.departamento_id)
        except:
            try:
                context['departamentoprofissional_list'] = DepartamentoProfissional.objects.filter(departamento__empresa_id=self.request.user.userProfile.empresa_id)
            except:
                redirect('/core/atendimento/list')
            
        atendimentos = []
        for prof in context['departamentoprofissional_list']:
            atendimento = Atendimento.objects.filter(departamentoProfissional_id=prof.pk)
            if atendimento.exists():
                atendimentos.append(atendimento)
            else:
                atend = Atendimento()
                atend.pk = 99999999
                atend.paciente_id = 1
                profissional = prof.pk
                atend.departamentoProfissional_id = profissional
                atend.tipoAtendimento_id = 0

                atend.retorno = False
                atendimento.valor = Decimal(10)
                atends = []
                atends.append(atend)
                atendimentos.append(atends)
        # print(context['departamentoprofissional_list'][0].tipo_profissional)
        # print(context['departamentoprofissional_list'][0].profissional.tiposAtendimentos.values_list)
        # print(atendimentos[0].last().escalaIntervalo)
        context['atendimentos'] = atendimentos
        # print(context['atendimentos'])
        # context['profissionais'] = DepartamentoProfissional.objects.select_related('')
        # print(dir(context['profissionais'][1].tipo_profissional))
        # # print(context)
        return context

    @method_decorator(permission_required(['global_permissions.ver_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendimentoListView, self).dispatch(*args, **kwargs)

class AtendimentoCreateView(MyCreateViewAtendimento):
    template_name = 'atendimento/templates/create_view_atendimento.html'
    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendimentoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.criar_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendimentoCreateView, self).dispatch(*args, **kwargs)

class AtendimentoUpdateView(MyUpdateViewAtendimento):
    template_name = 'atendimento/templates/create_view_atendimento.html'
    permission_required('se', raise_exception=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional = Profissional.objects.get(pk=self.object.pk)
        print(dir(profissional.tiposAtendimentos.first()))
        context['profissional'] = profissional
        escalas = Escala.objects.filter(departamentoProfissional_id=self.object.pk)
        pacientes = Paciente.objects.filter(departamento_id=self.object.departamento_id)
        intervalos = []

        for escala in escalas:
            intervalo = escala.escalaintervalo_set.filter(escala_id=escala.pk)
            atendimento_anterior = None
            for inter in intervalo:
                if inter.atendimento != None:
                    atendimento = Atendimento.objects.get(pk=inter.atendimento)
                    b = {'id': inter.pk,
                         'title': atendimento.paciente.nome.split(" ")[0],
                         'start': str(escala.dia) + "T" + str(inter.inicio),
                         'end': str(escala.dia) + "T" + atendimento.fim_atendimento.strftime("%H:%M"),
                         'className': "fc-danger",
                         'cliente': atendimento.paciente.nome.split(" ")[0],
                         'inicio': atendimento.inicio_atendimento.strftime("%Hh%M"),
                         'tipo_atendimento': atendimento.tipoAtendimento.tipo_atendimento.descricao,
                         'fim': atendimento.fim_atendimento.strftime("%Hh%M")
                         }
                    if (
                            inter.atendimento == atendimento_anterior):  # Verifica se é um atendimento em sequência de intervalos
                        continue

                    atendimento_anterior = inter.atendimento #Armazena o primeiro e id de um atendimento em sequencia de intervalos
                else:
                    b = {'id': inter.pk,
                         'title': "Disponível",
                         'start': str(escala.dia) + "T" + str(inter.inicio),
                         'end': str(escala.dia) + "T" + str(inter.fim),
                         'description': inter.descricao,
                         'className': "fc-success"
                         }
                intervalos.append(b)
        context['clientes'] = pacientes
        context['intervalos'] = intervalos
        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendimentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)

    @method_decorator(permission_required(['global_permissions.editar_atendimentos'], raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(AtendimentoUpdateView, self).dispatch(*args, **kwargs)

@login_required
def addAtendimento(request):
    if not request.POST.get('tipo_atendimento'):
        messages.error(request, "Selecione o tipo de atendimento")
    elif not request.POST.get('cliente'):
        messages.error(request, "Selecione um paciente")
    else:
        atendimento = Atendimento()
        atendimento.paciente_id = int(request.POST.get('cliente'))
        profissional = DepartamentoProfissional.objects.get(profissional_id=request.POST.get('profissional'))
        atendimento.departamentoProfissional = profissional
        atendimento.tipoAtendimento_id = request.POST.get('tipo_atendimento').split('-')[0] # split [0] é o id, [1] é o valor padrao [2] é tempo padrao
        if request.POST.get('retorno') == 1:
            atendimento.retorno = True
        else:
            atendimento.retorno = False
        atendimento.valor = Decimal(str(request.POST.get('valor')).replace(",", "."))
        atendimento.tempo = request.POST.get('tipo_atendimento').split('-')[2]
        atendimento.save()
        escala_intervalo_inicial = EscalaIntervalo.objects.get(pk=request.POST.get('id_escala_intervalo'))
        escalas_intervalo = None

        inicio = datetime.strptime(escala_intervalo_inicial.escala.dia.strftime("%Y-%m-%d") + " " + escala_intervalo_inicial.inicio.strftime("%H:%M:%S"),
                                   '%Y-%m-%d %H:%M:%S') # Datetime do início do primeiro intervalo
        horas = int(request.POST.get('tipo_atendimento').split('-')[2].split(':')[0]) # Quantidade de horas do tipo de atendimento
        minutos = int(request.POST.get('tipo_atendimento').split('-')[2].split(':')[1]) # Quantidade de minutos do tipo de atendimento
        fim = inicio + timedelta(minutes=(horas * 60 + minutos)-10) # inicio do ultimo intervalo

        atendimento.inicio_atendimento = inicio # Início do primeiro intervalo
        atendimento.fim_atendimento = fim + timedelta(minutes=10) # fim do ultimo intervalo
        atendimento.intervalo_id = request.POST.get('id_escala_intervalo')
        atendimento.pago = True
        atendimento.save()

        # Calcula quantidade de intervalos disponíveis necessários para completar a operação
        quantidade_intervalos_necessarios = int(request.POST.get('tipo_atendimento').split('-')[2].split(':')[0])*6
        # if int(request.POST['tipo_atendimento'].split('-')[2].split(':')[1]) == 30:
        #     quantidade_intervalos_necessarios += 1
        quantidade_intervalos_necessarios += (int(request.POST.get('tipo_atendimento').split('-')[2].split(':')[1]))/10
        # Fim do calculo de quantidade de intervalos


        escalas_todos_intervalos = EscalaIntervalo.objects.filter(escala_id=escala_intervalo_inicial.escala_id,
                                                                  inicio__range=[inicio, fim],atendimento=None).order_by(
                                                                  "inicio")  # Filtrar os intervalos de tempo de acordo com o atendimento


        if escalas_todos_intervalos.count() >= quantidade_intervalos_necessarios:
            departamento_profissional_paciente=''
            for intervalo in escalas_todos_intervalos:
                intervalo.atendimento = atendimento.pk
                pacienteDoMedico = PacienteDepartamentoProfissional.objects.get_or_create(paciente=atendimento.paciente,departamentoProfissional_id=atendimento.departamentoProfissional.pk)
                intervalo.save()
                if intervalo != len(escalas_todos_intervalos) - 1:
                    departamento_profissional_paciente=PacienteDepartamentoProfissional.objects.get(paciente=atendimento.paciente,departamentoProfissional_id=atendimento.departamentoProfissional.pk)
            prontuario = Prontuario.objects.get_or_create(atendimento=atendimento, departamento_profissional_paciente=departamento_profissional_paciente)
            messages.success(request, 'Atendimento marcado com sucesso')

        else:
            atendimento.delete()

            messages.error(request, "Para marcar este tipo de consulta você precisa de " +
                           request.POST['tipo_atendimento'].split('-')[2] + " disponíveis")
        # dict_obj = model_to_dict(atendimento)

        # subs = json.dumps(dict_obj)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponse(subs)

@login_required()
def desmarcarAtendimento(request):
    intervalo = request.POST.get('intervalolimpar')

    intervalo_obj = EscalaIntervalo.objects.get(pk=intervalo)
    if intervalo_obj.atendimento is not None:
        atendimento = Atendimento.objects.get(pk=intervalo_obj.atendimento)
        intervalos_obj = EscalaIntervalo.objects.filter(atendimento=intervalo_obj.atendimento)
        if atendimento.pago is not False:
            for inter in intervalos_obj:
                inter.atendimento = None
                inter.save()
            atendimento.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
