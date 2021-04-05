import re
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from core.models import Escala, EscalaIntervalo, Atendimento
from core.modulos.escala.form_escala import EscalaForm
from core.modulos.profissional.profissional import DepartamentoProfissional
from core.util.labels_property import LabesProperty


class MyGenericView(object):
    model = Escala
    form_class = EscalaForm
    success_url = reverse_lazy('core:modulo:escala:list_view')
    search_fields = ['departamentoProfissional']
    COLUMNS = [LabesProperty.PROFISSIONAL]
    NAME_MODEL = Escala._meta.verbose_name
    NAME_MODEL_PLURAL = Escala._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:escala:create_view')


@login_required
def addEditEscala(request):
    subs = {}
    if request.POST['editando'] == '1':
        id = request.POST['idbd']
        escala_intervalo = EscalaIntervalo.objects.get(pk=id)
        profissional = request.POST['profissional']
        datastart = request.POST['datastarte']
        dataend = request.POST['dataende']
        horastart = request.POST['horastarte']
        horaend = request.POST['horaende']
        descricao = request.POST['descricao']
        cor = request.POST['color']

        # Editar Model
        escala = Escala.objects.get(pk=escala_intervalo.escala_id)
        start = datetime.strptime(datastart + " " + horastart, '%d/%m/%Y %H:%M')
        end = datetime.strptime(dataend + " " + horaend, '%d/%m/%Y %H:%M')
        escala_intervalo.cor = cor
        escala_intervalo.descricao = descricao
        escala_intervalo.inicio = start
        escala_intervalo.fim = end
        if start.timestamp() < end.timestamp():
            escala_intervalo.save()
        else:
            pass
    # Criando pela primeira vez
    elif request.POST['editando'] == '0':
        profissional = request.POST['profissional']
        datastart = request.POST['datastart']
        dataend = request.POST['dataend']
        horastart = request.POST['horastart']
        horaend = request.POST['horaend']
        descricao = request.POST['descricao']
        cor = request.POST['color']
        print(datastart + " " + horastart)
        start = datetime.strptime(datastart + " " + horastart, '%d/%m/%Y %H:%M' )
        end = datetime.strptime(dataend + " " + horaend, '%d/%m/%Y %H:%M')
        print(profissional)
        departamento = request.user.userProfile.departamento_id
        depatamentoProfissional = DepartamentoProfissional.objects.get(departamento_id=departamento, profissional_id=profissional)

        if start.timestamp() < end.timestamp():
            escala = Escala.objects.get_or_create(dia=start.date(), departamentoProfissional_id=depatamentoProfissional.pk)
            escala[0].save()
            intervalostart = start.hour * 6  # Quantidade de intervalos inicialmente
            intervalostart = intervalostart + (start.minute / 10)
            intervaloend = end.hour * 6
            intervaloend = intervaloend + (end.minute / 10)  # Quantidade de intervalos finalmente
            diferenca_intervalo = int(intervaloend) - int(
                intervalostart)  # Diferença entre quantidade de intervalos iniciais e finais
            exists = False
            for i in range(int(diferenca_intervalo)):
                inicio = (start + timedelta(minutes=(i * 10)))
                fim = (start + timedelta(minutes=(i * 10) + 10))
                exists = EscalaIntervalo.objects.filter(inicio=inicio.strftime('%H:%M'), escala=escala[
                    0]).exists()  # Verifica se já existe esse intervalo
                if exists:
                    messages.error(request,
                                   "Não foi possível concluir essa operação, pois essa escala já existe no horário " + inicio.strftime(
                                       '%H:%M'))
                    break
                EscalaIntervalo(inicio=inicio.strftime('%H:%M'), fim=fim.strftime('%H:%M'), escala_id=escala[0].pk,
                                descricao=descricao, cor=cor).save()
            if not exists:
                if diferenca_intervalo > 1:
                    messages.success(request, "Escalas adicionadas com sucesso")
                elif diferenca_intervalo == 1:
                    messages.success(request, "Escala adicionada com sucesso")
                else:
                    messages.error(request, "O intervalo da escala precisa ter no mínimo 10 minutos")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def limparIntervalo(request):
    intervalo = request.POST['intervalolimpar']

    intervalo_obj = EscalaIntervalo.objects.get(pk=intervalo)
    if intervalo_obj.atendimento_id is not None and intervalo_obj.atendimento.pago == False:
        atendimento = Atendimento.objects.get(pk=intervalo_obj.atendimento_id)
        intervalos_obj = EscalaIntervalo.objects.filter(atendimento_id=intervalo_obj.atendimento)
        for inter in intervalos_obj:
            inter.delete()
        atendimento.delete()
    else:
        intervalo_obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def limparIntervaloDia(request):
    intervalo = request.POST.get('intervalolimpardia')
    intervalos = EscalaIntervalo.objects.filter(escala__dia=intervalo)

    for intervalo_obj in intervalos:
        # if intervalo_obj.atendimento_id is not None and intervalo_obj.atendimento.pago == False:
        #     atendimento = Atendimento.objects.get(pk=intervalo_obj.atendimento_id)
        #     intervalos_obj = EscalaIntervalo.objects.filter(atendimento_id=intervalo_obj.atendimento)
        #     for inter in intervalos_obj:
        #         inter.delete()
        #     atendimento.delete()
        # else:
        if intervalo_obj.atendimento is None:
            intervalo_obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def mobile(request):

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False