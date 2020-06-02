import calendar
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from core.models import Escala, EscalaIntervalo, Profissional, Atendimento
from core.modulos.escala.form_escala import EscalaForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyGenericView(object):
    model = Escala
    form_class = EscalaForm
    success_url = reverse_lazy('core:modulo:escala:list_view')
    search_fields = ['departamentoProfissional']
    COLUMNS = [LabesProperty.PROFISSIONAL]
    NAME_MODEL = Escala._meta.verbose_name
    NAME_MODEL_PLURAL = Escala._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:modulo:escala:create_view')


class MyListViewEscala(MyGenericView, LoginRequiredMixin, MyListViewSearcheGeneric, MyLabls, ListView):
    allow_empty = True


class MyCreateViewEscala(MyGenericView, LoginRequiredMixin, MyLabls, CreateView):
    pass


class MyUpdateViewEscala(MyGenericView, LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class EscalaCreateView(MyCreateViewEscala):
    template_name = 'escala/templates/create_view_escala.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['intervalos'] = []
        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        print(form.data)
        return super(EscalaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class EscalaUpdateView(MyUpdateViewEscala):
    template_name = 'escala/templates/create_view_escala.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.object.departamentoProfissional_id)
        profissional = Profissional.objects.get(pk=self.object.departamentoProfissional_id)
        context['idProfissional'] = profissional.pk
        escalas = Escala.objects.filter(departamentoProfissional_id=profissional.pk)
        intervalos = []
        for escala in escalas:
            intervalo = escala.escalaintervalo_set.get(escala_id=escala.pk)

            b = {'id': escala.pk,
                'title': "Disponível",
                 'start':str(escala.dia) + "T" + str(intervalo.inicio),
                 'end': str(escala.dia) + "T" + str(intervalo.fim),
                 'description': intervalo.descricao,
                 'className': "fc-"+intervalo.cor
                 }
            intervalos.append(b)
        # print(intervalos)
        context['intervalos'] = intervalos
        return context

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(EscalaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        print(self.request.POST)
        return super().form_valid(form)


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

        #Editar Model
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
        start = datetime.strptime(datastart + " " + horastart , '%d/%m/%Y %H:%M')
        end = datetime.strptime(dataend + " " + horaend , '%d/%m/%Y %H:%M')

        if start.timestamp() < end.timestamp():
            escala = Escala.objects.get_or_create(dia=start.date(),departamentoProfissional_id=profissional)
            escala[0].save()
            intervalostart = start.hour*2
            intervalostart = intervalostart+(start.minute/30)
            intervaloend = end.hour * 2
            intervaloend = intervaloend + (end.minute / 30)
            diferenca_intervalo = int(intervaloend) - int(intervalostart)
            if(diferenca_intervalo > 1):
                messages.success(request, "Escalas adicionadas com sucesso")
            elif(diferenca_intervalo == 1):
                messages.success(request, "Escala adicionada com sucesso")
            else:
                messages.error(request, "O intervalo da escala precisa ter no mínimo 30 minutos")


            for i in range(int(diferenca_intervalo)):
                inicio = (start + timedelta(minutes=(i * 30)))
                fim = (start + timedelta(minutes=(i * 30)+30))
                EscalaIntervalo(inicio=inicio.strftime('%H:%M'),fim=fim.strftime('%H:%M'),escala_id=escala[0].pk,descricao=descricao,cor=cor).save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required()
def limparIntervaloDia(request):
    intervalo = request.POST['intervalolimpar']

    intervalo_obj = EscalaIntervalo.objects.get(pk=intervalo)
    if(intervalo_obj.atendimento != None):
        atendimento = Atendimento.objects.get(pk=intervalo_obj.atendimento_id)
        intervalos_obj = EscalaIntervalo.objects.filter(atendimento_id=intervalo_obj.atendimento)
        for inter in intervalos_obj:
            inter.delete()
        atendimento.delete()
    else:
        intervalo_obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

