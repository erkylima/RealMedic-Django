from django.db import models

from core.util.util_manager import UpperCaseCharField


class AreaAtendimento(models.Model):
    class Meta:
        verbose_name = 'AREA ATENDIMENTO'
        verbose_name_plural = 'AREAS ATENDIMENTOS'

    descricao = UpperCaseCharField(u'Descricao', max_length=255)

    def __str__(self):
        return '{}'.format(self.descricao)
