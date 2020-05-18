from django.contrib.auth.models import User, Group
from django.db import models

from core.models import DepartamentoProfissional
from core.modulos.atendimento.atendimento import Atendimento

from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField


class Escala(Timestampable):
    class Meta:
        verbose_name = 'ESCALA'
        verbose_name_plural = 'ESCALAS'

    departamentoProfissional = models.ForeignKey(DepartamentoProfissional, on_delete=models.PROTECT)
    dia = models.DateField()

    @property
    def getNamePerfil(self):
        return self.departamentoProfissional.profissional.nome

    @property
    def getListAtributes(self):
        atributos = [ 'getNamePerfil',]
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista

class EscalaIntervalo(models.Model):
    escala = models.ForeignKey(Escala, on_delete=models.PROTECT)
    inicio = models.TimeField()
    fim = models.TimeField()
    descricao = models.CharField(max_length=255)
    cor = models.CharField(max_length=20)
    atendimento = models.ForeignKey(Atendimento, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def getListAtributes(self):
        atributos = ['inicio', 'fim']
        inter_lista = []
        for row in atributos:
            field_name = row
            field_object = EscalaIntervalo._meta.get_field(field_name)
            field_value = getattr(self, field_object.attname)
            inter_lista.append(field_value)
        return inter_lista