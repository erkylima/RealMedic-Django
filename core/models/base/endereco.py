from django.db import models

from core.util.util_manager import UpperCaseCharField


class Endereco(models.Model):
    class Meta:
        verbose_name = 'ENDEREÇO'
        verbose_name_plural = 'ENDEREÇOS'

    rua = UpperCaseCharField(u'Rua', max_length=255)
    bairro = UpperCaseCharField(u'Bairro', max_length=100)
    cidade = UpperCaseCharField(u'Cidade', max_length=100)
    estado = UpperCaseCharField(u'Estado', max_length=2)
    numero = UpperCaseCharField(u'Nº', max_length=50)

    def __str__(self):
        return '{} - {}'.format(self.rua, self.bairro)
