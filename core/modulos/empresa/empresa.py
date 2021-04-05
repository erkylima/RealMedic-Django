from django.db import models

from core.models.base.time_stampable import Timestampable


class Empresa(Timestampable):
    class Meta:
        verbose_name = 'EMPRESA'
        verbose_name_plural = 'EMPRESAS'

    nome_razao_social = models.CharField('Nome/Razão Social', max_length=255)
    documento = models.CharField('Documento',unique=True,max_length=18)

    def __str__(self):
        return self.nome_razao_social.upper()

    @property
    def getListAtributes(self):
        atributos = ['nome_razao_social', 'documento']
        inter_lista = []
        for row in atributos:
            field_name = row
            field_object = Empresa._meta.get_field(field_name)
            field_value = getattr(self, field_object.attname)
            inter_lista.append(field_value)
        return inter_lista

