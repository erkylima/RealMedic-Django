from django.contrib.auth.models import User, Group
from django.db import models

from core.models import Departamento
from core.models.base.time_stampable import Timestampable
from core.modulos.cliente.cliente import Cliente
from core.modulos.escala.escala import EscalaIntervalo
from core.modulos.profissional.profissional import DepartamentoProfissional
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento
from core.util.util_manager import UpperCaseCharField


class Atendimento(Timestampable):
    class Meta:
        verbose_name = 'ATENDIMENTO'
        verbose_name_plural = 'ATENDIMENTOS'

    escalaIntervalo = models.OneToOneField(EscalaIntervalo, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipoAtendimento = models.ForeignKey(TipoAtendimento, on_delete=models.PROTECT)
    departamentoProfissional = models.ForeignKey(DepartamentoProfissional, on_delete=models.PROTECT)



