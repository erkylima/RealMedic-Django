from django.db import models
from django.forms import CharField
from django.utils import timezone

from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.time_stampable import Timestampable
from core.modulos.departamento.departamento import Departamento
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento


class AtendimentosDepartamento(Timestampable):
    class Meta:
        verbose_name = 'ATENDIMENTO DO DEPARTAMENTO'
        verbose_name_plural = 'ATENDIMENTOS DO DEPARTAMENTO'
    departamento  = models.ForeignKey(Departamento, on_delete=models.PROTECT, default=1)
    nome = models.CharField('Nome', max_length=255, blank=True, null=True)
    tipo_profissional = models.IntegerField()
    tipo_atendimento = models.ForeignKey(TipoAtendimento, on_delete=models.PROTECT, default=1)
    tempo_padrao = models.TimeField(verbose_name='Tempo Padrão',default=timezone.now)
    valor_padrao = models.DecimalField(verbose_name='Preço Padrão',decimal_places=2,max_digits=5, default=0)
    publico = models.BooleanField(default=False)

    def __str__(self):
        return self.tipo_atendimento.descricao

    def getDescricao(self):
        return self.tipo_atendimento.descricao

    @property
    def getDepartamento(self):
        return self.departamento

    @property
    def getListAtributes(self):
        atributos = ['getDescricao', 'getDepartamento']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista