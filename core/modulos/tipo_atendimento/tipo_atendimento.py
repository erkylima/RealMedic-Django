from django.db import models
from datetime import datetime

from django.utils import timezone

from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField


class TipoAtendimento(Timestampable):
    class Meta:
        verbose_name = 'TIPO DE ATENDIMENTO'
        verbose_name_plural = 'TIPOS DE ATENDIMENTOS'

    descricao = UpperCaseCharField('Descrição', max_length=255)
    areaAtendimento = models.ForeignKey(AreaAtendimento,
                                        on_delete=models.PROTECT, verbose_name='Area de Atendimento')
    tempo_padrao = models.TimeField(verbose_name='Tempo Padrão',default=timezone.now)
    valor_padrao = models.DecimalField(verbose_name='Preço Padrão',decimal_places=2,max_digits=5, default=0)

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