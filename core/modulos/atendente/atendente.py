from django.contrib.auth.models import User, Group
from django.db import models

from core.models import Departamento
from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField


class Atendente(Timestampable):
    class Meta:
        verbose_name = 'ATENDENTE'
        verbose_name_plural = 'ATENDENTES'

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='userAtendente')
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='atendentes',
                                     null=True, blank=True)
    nome = UpperCaseCharField('Nome', max_length=255)
    usuario = UpperCaseCharField('Usuario', max_length=255, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    senha = UpperCaseCharField('Senha', max_length=255)
    perfil = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Perfil', related_name='atendentes')
    ativo = models.BooleanField(default=True)

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
