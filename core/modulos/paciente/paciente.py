from core.models.base.time_stampable import Timestampable
from django.db import models

from core.modulos.departamento.departamento import Departamento
from core.modulos.profissional.profissional import DepartamentoProfissional


class Paciente(Timestampable):
    class Meta:
        verbose_name = 'PACIENTE'
        verbose_name_plural = 'PACIENTES'

    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    nome = models.CharField('Nome', max_length=80)
    mae = models.CharField('Nome da Mãe', max_length=80, null=True, blank=True)
    email = models.CharField('Email', max_length=255)
    idade = models.IntegerField('Idade',default=10)
    telefone = models.CharField('Telefone', max_length=40, default='(87) 912345678')
    genero = models.IntegerField('Genero', default=1)
    endereco = models.CharField('Endereço', max_length=255,blank=True, null=True)
    sobre = models.CharField('Sobre', max_length=255,blank=True,default='')
    cliente_app = models.CharField('Cliente App', max_length=255, default=None, blank=True)

    def __str__(self):
        return self.nome

    @property
    def getDepartamento(self):
        return self.departamento

    @property
    def getListAtributes(self):
        atributos = ['nome', 'getDepartamento']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista


class PacienteDepartamentoProfissional(Timestampable):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    departamentoProfissional = models.ForeignKey(DepartamentoProfissional, on_delete=models.PROTECT)

    def __str__(self):
        return self.paciente.nome + ' paciente de ' + self.departamentoProfissional.profissional.nome

    @property
    def getNome(self):
        return self.paciente.nome

    @property
    def getEmail(self):
        return self.paciente.email

    @property
    def getListAtributes(self):
        atributos = ['getNome','getEmail']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista