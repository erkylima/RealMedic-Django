from django.contrib import admin

# Register your models here.
from core.models import Empresa, UserProfile
from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.lat_lng import LatLng
from core.modulos.atendente.atendente import Atendente
from core.modulos.atendimento.atendimento import Atendimento
from core.modulos.cliente.cliente import Cliente
from core.modulos.departamento.departamento import Departamento
from core.modulos.escala.escala import Escala, EscalaIntervalo
from core.modulos.profissional.profissional import Profissional, DepartamentoProfissional
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento
from core.modulos.tipo_profissional.tipo_profissional import TipoProfissional

# BASE
admin.site.register(AreaAtendimento)
admin.site.register(LatLng)
admin.site.register(Empresa)
admin.site.register(UserProfile)
admin.site.register(Profissional)
admin.site.register(Departamento)
admin.site.register(Atendente)
admin.site.register(Cliente)
admin.site.register(TipoAtendimento)
admin.site.register(TipoProfissional)
admin.site.register(DepartamentoProfissional)
admin.site.register(Escala)
admin.site.register(EscalaIntervalo)
admin.site.register(Atendimento)

