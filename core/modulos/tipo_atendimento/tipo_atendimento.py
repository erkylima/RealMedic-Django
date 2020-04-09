from django.db import models

from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField


class TipoAtendimento(Timestampable):
    class Meta:
        verbose_name = 'TIPO DE ATENDIMENTO'
        verbose_name_plural = 'TIPOS DE ATENDIMENTOS'

    descricao = UpperCaseCharField('DESCRIÇÃO', max_length=255)

    def __str__(self):
        return self.descricao
