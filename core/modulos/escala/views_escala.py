from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
import calendar
from core.models import Escala,EscalaIntervalo, Profissional
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
        escala = Escala.objects.get(pk=id)
        profissional = request.POST['profissional']
        datastart = request.POST['datastarte']
        dataend = request.POST['dataende']
        horastart = request.POST['horastarte']
        horaend = request.POST['horaende']
        descricao = request.POST['descricao']
        cor = request.POST['color']

        #Editar Model
        escala = Escala.objects.get(pk=id)
        escala_intervalo = EscalaIntervalo.objects.get(escala_id=escala.pk)
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
            escala = Escala.objects.get_or_create(dia=start)
            print(escala[0])
            escala[0].departamentoProfissional_id=profissional
            escala[0].save()

            escala_intervalo = EscalaIntervalo(inicio=start,fim=end,escala_id=escala[0].pk,descricao=descricao,cor=cor)
            escala_intervalo.save()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def marcarMes(request):
    print(calendar.monthrange(2012,6)[1])
    profissional = 1
    mes = 6
    for dia in range(calendar.monthrange(2012, mes)[1]):
        start = datetime.strptime("2020-" + str(mes).zfill(2) + "-" + str(dia+1).zfill(2) + " " + "08:00", '%Y-%m-%d %H:%M')
        escalas = Escala.objects.filter(departamentoProfissional_id=profissional, dia=start)

        escala_intervalo = EscalaIntervalo.objects.filter(escala=escala)
        for escala in escalas:
            for intervalo in escala_intervalo:
                escala = Escala


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
