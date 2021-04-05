from django.db import models

from core.models.base.endereco import Endereco
from core.models.base.time_stampable import Timestampable
from core.modulos.empresa.empresa import Empresa


class Departamento(Timestampable):
    class Meta:
        verbose_name = 'DEPARTAMENTO'
        verbose_name_plural = 'DEPARTAMENTOS'

    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name='empresa', null=True)
    nome = models.CharField('Nome', max_length=255)
    descricao = models.CharField('Descricao', max_length=255)
    endereco = models.ForeignKey(Endereco,models.PROTECT, null=True)

    def __str__(self):
        return self.empresa.nome_razao_social + " - " +self.nome.upper()

    @property
    def getEmpresa(self):
        return self.empresa.nome_razao_social

    def getNome(self):
        return self.empresa.nome_razao_social + " - " +self.nome.upper()

    @property
    def getListAtributes(self):
        atributos = ['nome', 'getEmpresa', 'descricao']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista
