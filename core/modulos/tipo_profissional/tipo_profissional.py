from django.contrib.auth.models import User, Group
from django.db import models

from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.time_stampable import Timestampable
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento
from core.util.util_manager import UpperCaseCharField


class TipoProfissional(Timestampable):
    class Meta:
        verbose_name = 'TIPO DE PROFISSIONAL'
        verbose_name_plural = 'TIPOS DE PROFISSIONAIS'

    descricao = UpperCaseCharField('Descrição', max_length=255)
    areaAtendimento = models.ForeignKey(AreaAtendimento,
                                        on_delete=models.PROTECT)
    tiposAtendimentos = models.ManyToManyField(TipoAtendimento)
