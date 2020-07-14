from django.contrib.auth.models import User, Group
from django.db import models

from core.models import Departamento, TipoProfissional, TipoAtendimento
from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField

class Profissional(Timestampable):
    class Meta:
        verbose_name = 'PROFISSIONAL'
        verbose_name_plural = 'PROFISSIONAIS'

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='userProfissional')
    nome = UpperCaseCharField('Nome', max_length=255)
    codigo = UpperCaseCharField('Código', max_length=10,default="")
    usuario = UpperCaseCharField('Usuario', max_length=255, unique=True)
    email = models.EmailField('Email', max_length=255, unique=True)
    senha = UpperCaseCharField('Senha', max_length=255)
    perfil = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Perfil', related_name='profissionais')
    ativo = models.BooleanField(default=True)
    tiposAtendimentos = models.ManyToManyField(TipoAtendimento, verbose_name='Tipos de Atendimento')


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

class DepartamentoProfissional(models.Model):
    # class Meta:
    #     verbose_name = 'PROFISSIONAL'
    #     verbose_name_plural = 'PROFISSIONAIS'

    profissional = models.ForeignKey(Profissional, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    tipo_profissional = models.ForeignKey(TipoProfissional, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.profissional.nome
