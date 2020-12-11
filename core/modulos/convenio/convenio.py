from django.contrib.auth.models import User, Group
from django.db import models

from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField


class Convenio(Timestampable):
    class Meta:
        verbose_name = 'CONVENIO'
        verbose_name_plural = 'CONVENIOS'
    nome = models.CharField("Nome",max_length=100)
    descricao = UpperCaseCharField('Descrição', max_length=255)
    desconto = models.IntegerField('Desconto')

    def __str__(self):
        return self.nome

    @property
    def getListAtributes(self):
        atributos = ['descricao']
        inter_lista = []
        for row in atributos:
            field_name = row
            field_object = Convenio._meta.get_field(field_name)
            field_value = getattr(self, field_object.attname)
            inter_lista.append(field_value)
        return inter_lista