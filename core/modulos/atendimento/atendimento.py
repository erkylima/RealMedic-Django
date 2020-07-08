from django.db import models
from django.utils import timezone

from core.models.base.time_stampable import Timestampable
from core.modulos.paciente.paciente import Paciente

from core.modulos.profissional.profissional import DepartamentoProfissional
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento


class Atendimento(Timestampable):
    class Meta:
        verbose_name = 'ATENDIMENTO'
        verbose_name_plural = 'ATENDIMENTOS'

    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, default=1)
    tipoAtendimento = models.ForeignKey(TipoAtendimento, on_delete=models.PROTECT)
    departamentoProfissional = models.ForeignKey(DepartamentoProfissional, on_delete=models.PROTECT)
    retorno = models.BooleanField(default=False)
    valor = models.DecimalField(verbose_name='Preço',decimal_places=2,max_digits=5, default=0)
    tempo = models.TimeField(default=timezone.now)
    inicio_atendimento = models.TimeField(null=True, blank=True) # Horario de inicialização do atendimento
    fim_atendimento = models.TimeField(null=True, blank=True) # Horario de finalização do atendimento

    def __str__(self):
        return self.paciente.nome

    @property
    def getNamePerfil(self):
        return self.paciente.nome

    @property
    def getDataAtendimento(self):
        return self.escalaintervalo_set.first().escala.dia.strftime('%d/%m/%Y às ') + self.escalaintervalo_set.first().inicio.strftime("%H:%M até ") + \
               self.escalaintervalo_set.first().fim.strftime("%H:%M")


    @property
    def getListAtributes(self):
        atributos = ['getNamePerfil', 'tipoAtendimento', 'valor','getDataAtendimento']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista

