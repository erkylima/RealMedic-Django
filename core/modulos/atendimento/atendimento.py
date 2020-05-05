from datetime import datetime

from django.contrib.auth.models import User, Group
from django.db import models

from core.models import Departamento
from core.models.base.time_stampable import Timestampable
from core.modulos.cliente.cliente import Cliente
from core.modulos.profissional.profissional import DepartamentoProfissional
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento
from core.util.util_manager import UpperCaseCharField


class Atendimento(Timestampable):
    class Meta:
        verbose_name = 'ATENDIMENTO'
        verbose_name_plural = 'ATENDIMENTOS'

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipoAtendimento = models.ForeignKey(TipoAtendimento, on_delete=models.PROTECT)
    departamentoProfissional = models.ForeignKey(DepartamentoProfissional, on_delete=models.PROTECT)
    retorno = models.BooleanField(default=False)
    valor = models.DecimalField(verbose_name='Preço',decimal_places=2,max_digits=5, default=0)
    tempo = models.TimeField(default=datetime.now())

    def __str__(self):
        return self.cliente.nome


