from django.contrib.auth.models import User, Group
from django.db import models

from core.models import Departamento
from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField


class Cliente(Timestampable):
    class Meta:
        verbose_name = 'CLIENTE'
        verbose_name_plural = 'CLIENTES'

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='userCliente')
    nome = UpperCaseCharField('Nome', max_length=255)
    usuario = UpperCaseCharField('Usuario', max_length=255, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    senha = UpperCaseCharField('Senha', max_length=255)
    perfil = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Perfil', related_name='clientes')
    ativo = models.BooleanField(default=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT,default=1)
    # hasSuperAdministrador = models.BooleanField('Super', default=False)

    def __str__(self):
        return self.nome.upper()

    @property
    def getNamePerfil(self):
        return self.perfil.name

    @property
    def getListAtributes(self):
        atributos = ['nome', 'usuario', 'getNamePerfil']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista
