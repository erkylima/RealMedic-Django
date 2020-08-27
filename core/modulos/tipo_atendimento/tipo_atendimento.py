from django.db import models
from django.forms import CharField
from django.utils import timezone

from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.time_stampable import Timestampable
from core.modulos.departamento.departamento import Departamento
from core.modulos.tipo_profissional.tipo_profissional import TipoProfissional


class TipoAtendimento(Timestampable):
    class Meta:
        verbose_name = 'TIPO DE ATENDIMENTO GERAL'
        verbose_name_plural = 'TIPOS DE ATENDIMENTOS GERAL'
    tipo_profissional = models.ForeignKey(TipoProfissional, on_delete=models.PROTECT, default=1)
    descricao = models.CharField('Descricao', max_length=255)
    areaAtendimento = models.ForeignKey(AreaAtendimento,
                                        on_delete=models.PROTECT, verbose_name='Area de Atendimento')

    def __str__(self):
        return self.descricao

    @property
    def getListAtributes(self):
        atributos = ['descricao']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista