from django.db import models

from core.models.base.time_stampable import Timestampable
from core.modulos.user_profile.user_profile import UserProfile


class Gerente(Timestampable):
    class Meta:
        verbose_name = 'GERENTE'
        verbose_name_plural = 'GERENTES'

    userProfile = models.OneToOneField(UserProfile, on_delete=models.PROTECT, related_name='gerente')


    # hasSuperAdministrador = models.BooleanField('Super', default=False)

    def __str__(self):
        return self.userProfile.nome.upper()

    def getJson(self):
        return dict(
            id=self.pk,
            nome=self.userProfile.nome,
            login=self.userProfile.usuario,
            tipo='ger',
            token=self.userProfile.getToken(),
        )
    @property
    def getNamePerfil(self):
        return self.userProfile.perfil.name

    @property
    def getListAtributes(self):
        atributos = ['nome', 'usuario', 'getNamePerfil']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista
