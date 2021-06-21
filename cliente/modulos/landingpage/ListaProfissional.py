from django.core.files.storage import FileSystemStorage

from core.models.base.time_stampable import Timestampable
from django.db import models

from core.modulos.tipo_profissional.tipo_profissional import TipoProfissional

class Pais(models.Model):
    class Meta:
        verbose_name = 'PAÍS'
        verbose_name_plural = 'PAÍSES'
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class ListaEmpresa(Timestampable):

    class Meta:
        verbose_name = 'Lista de Empresa LandingPage'
        verbose_name_plural = 'Lista de Empresa LandingPage'
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, default=1)
    nome = models.CharField(max_length=100,default='')
    nome_slug = models.CharField(max_length=50, default='all')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome.upper()

class Endereco(models.Model):
    empresa = models.ForeignKey(ListaEmpresa, on_delete=models.PROTECT, related_name='enderecos',default=1)
    nome = models.CharField(max_length=30)
    rua = models.CharField(max_length=100, default="")
    numero = models.IntegerField(default=0)
    cidade = models.CharField(max_length=50, default="")
    cep = models.IntegerField(default=0)
    uf = models.CharField(max_length=4)
    slug = models.SlugField()

    def __str__(self):
        return self.nome + "-" +self.uf

    def Endereco(self):
        return "Endereço da " + self.empresa.nome

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
    listaempresa = models.ManyToManyField(ListaEmpresa)
    nome = models.CharField(max_length=100,default='')
    especi = models.ManyToManyField(TipoProfissional, related_name='espec')
    agenda = models.CharField(max_length=100,default='')
    local_atendimento = models.CharField(max_length=100,default='')
    imagem = models.ImageField(upload_to='images/profs', name='', storage=OverwriteStorage(),default='')
    servicos = models.TextField(default='')
    ativo = models.BooleanField(default=True)
    telefone1 = models.CharField(max_length=50,default='')
    telefone2 = models.CharField(max_length=50, default='', null=True, blank=True)
    instagram = models.CharField(max_length=50, default='', null=True, blank=True)
    facebook = models.CharField(max_length=50, default='', null=True, blank=True)

    def __str__(self):
        return self.nome.upper()

    def Especialidades(self):
        return "\n, ".join([p.descricao for p in self.especi.all()])

    def getJson(self):
        return dict(
            id=self.pk,
            nome=self.nome,
        )

    @property
    def getNome(self):
        return self.nome

