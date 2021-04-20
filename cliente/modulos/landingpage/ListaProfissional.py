from django.core.files.storage import FileSystemStorage

from core.models.base.time_stampable import Timestampable
from django.db import models

class ListaEmpresa(Timestampable):
    class Meta:
        verbose_name = 'Lista de Empresa LandingPage'
        verbose_name_plural = 'Lista de Empresa LandingPage'
    nome = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.nome.upper()


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length):
        """
        Retorna um filename disponível para a class storage e
        o novo conteúdo para ser gravado
        """
        # Se o filename já existir, este é removido
        if self.exists(name):
            self.delete(name)
        return name


class ListaProfissional(Timestampable):
    class Meta:
        verbose_name = 'Lista de LandingPage'
        verbose_name_plural = 'Lista de LandingPage'
    listaempresa = models.ForeignKey(ListaEmpresa, on_delete=models.PROTECT,related_name='prof',default=1)
    nome = models.CharField(max_length=100,default='')
    especialidade = models.CharField(max_length=100,default='')
    agenda = models.CharField(max_length=100,default='')
    local_atendimento = models.CharField(max_length=100,default='')
    imagem = models.ImageField(upload_to='images/profs', storage=OverwriteStorage(),default='')

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

