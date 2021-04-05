from django.db import models

from core.models.base.time_stampable import Timestampable
from core.modulos.user_profile.user_profile import UserProfile



class Cliente(Timestampable):
    class Meta:
        verbose_name = 'CLIENTE'
        verbose_name_plural = 'CLIENTES'

    userProfile = models.OneToOneField(UserProfile, on_delete=models.PROTECT, related_name='cliente')

    cliente_app = models.CharField('Cliente App', max_length=255, default='', blank=True)
    # hasSuperAdministrador = models.BooleanField('Super', default=False)

    def __str__(self):
        return self.userProfile.nome.upper()

    def getJson(self):
        return dict(
            id=self.pk,
            nome=self.userProfile.nome,
            login=self.userProfile.usuario,
            tipo='cliente',
            token=self.userProfile.getToken(),
        )

    @property
    def getNamePerfil(self):
        return self.userProfile.perfil.name

    @property
    def getNome(self):
        return self.userProfile.nome

    def getUsuario(self):
        return self.userProfile.usuario

    @property
    def getListAtributes(self):
        atributos = ['getNome', 'getUsuario', 'getNamePerfil']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista
