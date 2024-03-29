from django.db import models

from core.models.base.time_stampable import Timestampable
from core.modulos.user_profile.user_profile import UserProfile


class Atendente(Timestampable):
    class Meta:
        verbose_name = 'ATENDENTE'
        verbose_name_plural = 'ATENDENTES'

    userProfile = models.OneToOneField(UserProfile, on_delete=models.PROTECT, related_name='atendente')



    # hasSuperAdministrador = models.BooleanField('Super', default=False)

    def __str__(self):
        return self.userProfile.nome.upper()

    @property
    def getDepartamento(self):
        return self.userProfile.departamento

    def getJson(self):
        return dict(
            id=self.pk,
            nome=self.userProfile.nome,
            login=self.userProfile.usuario,
            tipo='atendente',
            token=self.userProfile.getToken(),
        )

    @property
    def getNome(self):
        return self.userProfile.nome

    def getUsuario(self):
        return self.userProfile.usuario

    @property
    def getListAtributes(self):
        atributos = ['getNome', 'getUsuario', 'getDepartamento']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista
