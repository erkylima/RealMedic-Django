from django.db import models



class AreaAtendimento(models.Model):
    class Meta:
        verbose_name = 'AREA ATENDIMENTO'
        verbose_name_plural = 'AREAS ATENDIMENTOS'

    descricao = models.CharField('Descricao', max_length=255)

    def __str__(self):
        return '{}'.format(self.descricao)
