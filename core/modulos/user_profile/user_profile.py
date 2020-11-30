from django.contrib.auth.models import User, Group
from django.db import models

from core.models import Empresa
from core.models.base.time_stampable import Timestampable
from core.modulos.departamento.departamento import Departamento
from core.util.util_manager import UpperCaseCharField


class UserProfile(Timestampable):
    class Meta:
        verbose_name = 'USUARIO'
        verbose_name_plural = 'USUARIOS'

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='userProfile')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name='usuarios', null=True)
    nome = UpperCaseCharField('Nome', max_length=255)
    usuario = UpperCaseCharField('Usuario', max_length=255, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    senha = UpperCaseCharField('Senha', max_length=255)
    perfil = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Perfil', related_name='usuarios')
    ativo = models.BooleanField(default=True)

    # hasSuperAdministrador = models.BooleanField('Super', default=False)

    def __str__(self):
        return self.nome.upper()

    def getJson(self):
        return dict(
            id=self.pk,
            nome=self.nome,
            login=self.usuario,
            tipo='adm',
            token=self.getToken(),
        )

    def getToken(self):
        return self.user.auth_token.key

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
