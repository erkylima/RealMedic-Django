from core.models.base.time_stampable import Timestampable
from django.db import models

class ListaEmpresa(Timestampable):
    class Meta:
        verbose_name = 'Lista de Empresa LandingPage'
        verbose_name_plural = 'Lista de Empresa LandingPage'
    nome = models.CharField(max_length=100,default='')

class ListaProfissional(Timestampable):
    class Meta:
        verbose_name = 'Lista de LandingPage'
        verbose_name_plural = 'Lista de LandingPage'
    # listaempresa = models.ForeignKey(ListaEmpresa, on_delete=models.PROTECT,related_name='prof',default=1)
    nome = models.CharField(max_length=100,default='')
    especialidade = models.CharField(max_length=100,default='')
    agenda = models.CharField(max_length=100,default='')
    local_atendimento = models.CharField(max_length=100,default='')
    imagem = models.ImageField(upload_to='images/profs', default='')

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
