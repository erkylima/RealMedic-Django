from datetime import datetime, timedelta
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import View

from core.models import Atendimento, DepartamentoProfissional, Profissional, Escala, Cliente, EscalaIntervalo
from core.modulos.atendimento.form_atendimento import AtendimentoForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = DepartamentoProfissional
    form_class = AtendimentoForm
    success_url = reverse_lazy('cliente:modulo:marca_atendimento:list_view')
    search_fields = ['nome_razao_social', 'documento']
    COLUMNS = [LabesProperty.NOME, LabesProperty.DOCUMENTO]
    NAME_MODEL = Atendimento._meta.verbose_name
    NAME_MODEL_PLURAL = Atendimento._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('cliente:modulo:marca_atendimento:list_view')


class MyListViewAtendimento(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True

class MyDetailViewAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, View):
    pass

class MyCreateViewAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewAtendimento(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass

class AtendimentoListView(MyListViewAtendimento):
    template_name = 'marca_atendimento/templates/list_view_atendimento.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        atendimentos = []
        for prof in context['departamentoprofissional_list']:
            atendimento = Atendimento.objects.filter(departamentoProfissional_id=prof.pk)
            if atendimento.exists():
                atendimentos.append(atendimento)
            else:
                atend = Atendimento()
                atend.pk = 99999999
                atend.cliente_id = 1
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

class AtendimentoUpdateView(MyUpdateViewAtendimento):
    template_name = 'atendimento/templates/create_view_atendimento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profissional = Profissional.objects.get(pk=self.object.pk)
        context['profissional'] = profissional
        escalas = Escala.objects.filter(departamentoProfissional_id=self.object.pk)
        clientes = Cliente.objects.all()
        intervalos = []

        for escala in escalas:
            intervalo = escala.escalaintervalo_set.filter(escala_id=escala.pk)
            atendimento_anterior = None
            for inter in intervalo:
                if inter.atendimento_id != None:
                    b = {'id': inter.pk,
                         'title': inter.atendimento.cliente.nome.split(" ")[0],
                         'start': str(escala.dia) + "T" + str(inter.inicio),
                         'end': str(escala.dia) + "T" + inter.atendimento.fim_atendimento.strftime("%H:%M"),
                         'description': inter.descricao,
                         'className': "fc-danger",
                         'cliente': inter.atendimento.cliente.nome.split(" ")[0],
                         'inicio': inter.atendimento.inicio_atendimento.strftime("%Hh%M"),
                         'tipo_atendimento': inter.atendimento.tipoAtendimento.descricao,
                         'fim': inter.atendimento.fim_atendimento.strftime("%Hh%M")
                         }
                    if(inter.atendimento_id == atendimento_anterior):# Verifica se é um atendimento em sequência de intervalos
                        continue

                    atendimento_anterior = inter.atendimento_id #Armazena o primeiro e id de um atendimento em sequencia de intervalos
                else:
                    b = {'id': inter.pk,
                         'title': "Disponível",
                         'start': str(escala.dia) + "T" + str(inter.inicio),
                         'end': str(escala.dia) + "T" + str(inter.fim),
                         'description': inter.descricao,
                         'className': "fc-success"
                         }
                intervalos.append(b)

        context['clientes'] = clientes
        context['intervalos'] = intervalos
        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(AtendimentoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)


@login_required
def addAtendimento(request):
    if request.POST['tipo_atendimento'] == '':
        messages.error(request, "Selecione o tipo de atendimento")
    elif request.POST['cliente'] == '':
        messages.error(request, "Selecione um cliente")
    else:
        atendimento = Atendimento()
        atendimento.cliente_id = str(request.POST['cliente'])
        profissional = DepartamentoProfissional.objects.get(profissional_id=request.POST['profissional'])
        atendimento.departamentoProfissional = profissional
        atendimento.tipoAtendimento_id = request.POST['tipo_atendimento'].split('-')[0] # split [0] é o id, [1] é o valor padrao [2] é tempo padrao
        if request.POST['retorno'] == 1:
            atendimento.retorno = True
        else:
            atendimento.retorno = False
        atendimento.valor = Decimal(str(request.POST['valor']).replace(",", "."))
        atendimento.tempo = request.POST['tipo_atendimento'].split('-')[2]
        atendimento.save()
        escala_intervalo_inicial = EscalaIntervalo.objects.get(pk=request.POST['id_escala_intervalo'])
        escalas_intervalo = None

        inicio = datetime.strptime(escala_intervalo_inicial.escala.dia.strftime("%Y-%m-%d") + " " + escala_intervalo_inicial.inicio.strftime("%H:%M:%S"),
                                   '%Y-%m-%d %H:%M:%S') # Datetime do início do primeiro intervalo
        horas = int(request.POST['tipo_atendimento'].split('-')[2].split(':')[0]) # Quantidade de horas do tipo de atendimento
        minutos = int(request.POST['tipo_atendimento'].split('-')[2].split(':')[1]) # Quantidade de minutos do tipo de atendimento
        fim = inicio + timedelta(minutes=(horas * 60 + minutos) - 30) # inicio do ultimo intervalo

        atendimento.inicio_atendimento = inicio # Início do primeiro intervalo
        atendimento.fim_atendimento = fim + timedelta(minutes=30) # fim do ultimo intervalo
        atendimento.save()

        # Calcula quantidade de intervalos disponíveis necessários para completar a operação
        quantidade_intervalos_necessarios = int(request.POST['tipo_atendimento'].split('-')[2].split(':')[0])*2
        if int(request.POST['tipo_atendimento'].split('-')[2].split(':')[1]) == 30:
            quantidade_intervalos_necessarios += 1
        # Fim do calculo de quantidade de intervalos

        escalas_todos_intervalos = EscalaIntervalo.objects.filter(escala_id=escala_intervalo_inicial.escala_id,
                                                                  inicio__range=[inicio, fim],atendimento_id=None).order_by(
                                                                  "inicio")  # Filtrar os intervalos de tempo de acordo com o atendimento

        if escalas_todos_intervalos.count() >= quantidade_intervalos_necessarios:
            for intervalo in escalas_todos_intervalos:
                intervalo.atendimento_id = atendimento.pk
                intervalo.save()
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
    intervalo = request.POST['intervalolimpar']

    intervalo_obj = EscalaIntervalo.objects.get(pk=intervalo)
    if (intervalo_obj.atendimento != None):
        atendimento = Atendimento.objects.get(pk=intervalo_obj.atendimento_id)
        intervalos_obj = EscalaIntervalo.objects.filter(atendimento_id=intervalo_obj.atendimento)
        for inter in intervalos_obj:
            inter.atendimento_id = None
            inter.save()
        atendimento.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
