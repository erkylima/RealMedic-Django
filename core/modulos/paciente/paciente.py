from core.models.base.time_stampable import Timestampable
from django.db import models

from core.modulos.departamento.departamento import Departamento
from core.modulos.profissional.profissional import DepartamentoProfissional


class Paciente(Timestampable):
    class Meta:
        verbose_name = 'PACIENTE'
        verbose_name_plural = 'PACIENTES'

    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    nome = models.CharField('Nome', max_length=255)
    email = models.CharField('Email', max_length=255)
    cliente_app = models.CharField('Cliente App', max_length=255, default=None, blank=True)

    def __str__(self):
        return self.nome

    @property
    def getListAtributes(self):
        atributos = ['nome']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista


class PacienteDepartamentoProfissional(Timestampable):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    departamentoProfissional = models.ForeignKey(DepartamentoProfissional, on_delete=models.PROTECT)