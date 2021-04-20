from core.models.base.time_stampable import Timestampable
from django.db import models


class ListaProfissional(Timestampable):
    class Meta:
        verbose_name = 'Lista de LandingPage'
        verbose_name_plural = 'Lista de LandingPage'
    nome = models.CharField(max_length=100,default='')
    especialidade = models.CharField(max_length=100,default='')
    agenda = models.CharField(max_length=100,default='')
    local_atendimento = models.CharField(max_length=100,default='')
    imagem = models.ImageField(upload_to='core/')

    def __str__(self):
        return self.nome.upper()

    def getJson(self):
        return dict(
            id=self.pk,
            nome=self.nome,
        )

    @property
    def getNome(self):
        return self.nome
