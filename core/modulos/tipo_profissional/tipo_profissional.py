from django.contrib.auth.models import User, Group
from django.db import models

from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.time_stampable import Timestampable
from core.models import TipoAtendimento,Departamento
from core.util.util_manager import UpperCaseCharField


class TipoProfissional(Timestampable):
    class Meta:
        verbose_name = 'TIPO DE PROFISSIONAL'
        verbose_name_plural = 'TIPOS DE PROFISSIONAIS'

    descricao = UpperCaseCharField('Descrição', max_length=255)
    areaAtendimento = models.ForeignKey(AreaAtendimento,
                                        on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento,
                                        on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

    @property
    def getListAtributes(self):
        atributos = ['descricao']
        inter_lista = []
        for row in atributos:
            field_name = row
            field_object = TipoAtendimento._meta.get_field(field_name)
            field_value = getattr(self, field_object.attname)
            inter_lista.append(field_value)
        return inter_lista