from django.db import models
from django.utils import timezone

from core.models.base.time_stampable import Timestampable
from core.modulos.escala.escala import EscalaIntervalo
from core.modulos.paciente.paciente import Paciente

from core.modulos.profissional.profissional import DepartamentoProfissional
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento


class Atendimento(Timestampable):
    class Meta:
        verbose_name = 'ATENDIMENTO'
        verbose_name_plural = 'ATENDIMENTOS'

    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, default=1)
    tipoAtendimento = models.ForeignKey(TipoAtendimento, on_delete=models.PROTECT)
    intervalo = models.ForeignKey(EscalaIntervalo,on_delete=models.PROTECT,null=True, blank=True, related_name='escala_intervalo')
    departamentoProfissional = models.ForeignKey(DepartamentoProfissional, on_delete=models.PROTECT)
    retorno = models.BooleanField(default=False)
    valor = models.DecimalField(verbose_name='Preço',decimal_places=2,max_digits=5, default=0)
    tempo = models.TimeField(default=timezone.now)
    inicio_atendimento = models.TimeField(null=True, blank=True) # Horario de inicialização do atendimento
    fim_atendimento = models.TimeField(null=True, blank=True) # Horario de finalização do atendimento
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.paciente.nome

    @property
    def getNamePerfil(self):
        return self.paciente.nome

    @property
    def getDataAtendimento(self):
        return self.intervalo.escala.dia.strftime('%d/%m/%Y às ') + self.inicio_atendimento.strftime("%H:%M até ") + \
               self.fim_atendimento.strftime("%H:%M")


    @property
    def getListAtributes(self):
        atributos = ['getNamePerfil', 'tipoAtendimento', 'valor','getDataAtendimento']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista

