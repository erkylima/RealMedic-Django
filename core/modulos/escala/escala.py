from django.contrib.auth.models import User, Group
from django.db import models

from core.models import Departamento
from core.models.base.time_stampable import Timestampable
from core.modulos.profissional.profissional import DepartamentoProfissional
from core.util.util_manager import UpperCaseCharField


class Escala(Timestampable):
    class Meta:
        verbose_name = 'ESCALA'
        verbose_name_plural = 'ESCALAS'

    departamentoProfissional = models.ForeignKey(DepartamentoProfissional, on_delete=models.PROTECT)
    dia = models.DateField()


class EscalaIntervalo(Timestampable):
    escala = models.ForeignKey(Escala, on_delete=models.PROTECT)
    inicio = models.TimeField()
    fim = models.TimeField()
