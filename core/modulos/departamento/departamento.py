from django.db import models

from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField
from core.models import Empresa


class Departamento(Timestampable):
    class Meta:
        verbose_name = 'DEPARTAMENTO'
        verbose_name_plural = 'DEPARTAMENTOS'

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name='empresa', null=True)
    nome = UpperCaseCharField('Nome', max_length=255)
    descricao = UpperCaseCharField('Descricao', max_length=255)

    def __str__(self):
        return self.empresa.nome_razao_social + " - " +self.nome.upper()

    @property
    def getEmpresa(self):
        return self.empresa.nome_razao_social

    @property
    def getListAtributes(self):
        atributos = ['nome', 'getEmpresa', 'descricao']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista
