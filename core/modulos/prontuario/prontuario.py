from django.db import models

from core.models.base.time_stampable import Timestampable
from core.modulos.atendimento.atendimento import Atendimento
from core.modulos.paciente.paciente import PacienteDepartamentoProfissional


class Prontuario(Timestampable):

    class Meta:
        verbose_name = 'PRONTUARIO'
        verbose_name_plural = 'PRONTUARIOS'

    atendimento = models.OneToOneField(Atendimento, on_delete=models.PROTECT)
    departamento_profissional_paciente = models.ForeignKey(PacienteDepartamentoProfissional, on_delete=models.PROTECT)
    observacao = models.CharField('Observação', max_length=255,blank=True)

    def __str__(self):
        return 'Prontuario de {0}'.format(self.departamento_profissional_paciente.paciente.nome)

    @property
    def getNamePaciente(self):
        return '{0}'.format(self.departamento_profissional_paciente.paciente.nome)

    @property
    def getListAtributes(self):
        atributos = ['getNamePaciente', 'observacao']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista
