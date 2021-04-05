from django.contrib.auth.models import User, Group
from django.db import models

from core.models.base.time_stampable import Timestampable
from core.modulos.departamento.departamento import Departamento


class UserProfile(Timestampable): # Usuários com perfil no painel da clinica
    class Meta:
        verbose_name = 'USUARIO GERENCIA DE CLINICA'
        verbose_name_plural = 'USUARIOS GERENCIA DE CLINICA'

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='userProfile')
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True, blank=True)
    nome = models.CharField('Nome', max_length=255)
    usuario = models.CharField('Usuario', max_length=255, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    senha = models.CharField('Senha', max_length=255)
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

class UserComum(Timestampable): # Usuários com independecia do painel
    class Meta:
        verbose_name = 'USUARIO INDEPENDENTE DE CLINICA'
        verbose_name_plural = 'USUARIOS INDEPENDENTES DE CLINICA'

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='userComum')
    nome = models.CharField('Nome', max_length=255)
    usuario = models.CharField('Usuario', max_length=255, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    senha = models.CharField('Senha', max_length=255)
    perfil = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Perfil', related_name='usuarioComum')
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
