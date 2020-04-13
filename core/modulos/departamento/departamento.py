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
    areaAtendimento = models.ForeignKey(AreaAtendimento, on_delete=models.PROTECT, related_name='empresas', null=True)
    nome = UpperCaseCharField('Nome', max_length=255)
    descricao = UpperCaseCharField('Descricao', max_length=255)

    def __str__(self):
        return self.nome.upper()

    @property
    def getListAtributes(self):
        atributos = ['nome', 'descricao']
        inter_lista = []
        for row in atributos:
            field_name = row
            field_object = Departamento._meta.get_field(field_name)
            field_value = getattr(self, field_object.attname)
            inter_lista.append(field_value)
        return inter_lista
