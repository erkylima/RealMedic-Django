from django.db import models

from core.models.base.time_stampable import Timestampable
from core.modulos.paciente.paciente import PacienteDepartamentoProfissional


class Prontuario(Timestampable):

    class Meta:
        verbose_name = 'PRONTUARIO'
        verbose_name_plural = 'PRONTUARIOS'

    departamento_profissional_paciente = models.ForeignKey(PacienteDepartamentoProfissional, on_delete=models.PROTECT)
    observacao = models.CharField('Observação', max_length=255)
    peso = models.DecimalField(max_digits=5,decimal_places=2)

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
