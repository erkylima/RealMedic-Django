from django.db import models



class Endereco(models.Model):
    class Meta:
        verbose_name = 'ENDEREÇO'
        verbose_name_plural = 'ENDEREÇOS'

    rua = models.CharField(u'Rua', max_length=255, blank=True)
    bairro = models.CharField(u'Bairro', max_length=100, blank=True)
    cidade = models.CharField(u'Cidade', max_length=100, blank=True)
    estado = models.CharField(u'Estado', max_length=2, blank=True)
    numero = models.CharField(u'Nº', max_length=50, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.rua, self.bairro)
