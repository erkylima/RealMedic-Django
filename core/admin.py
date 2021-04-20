from django.contrib import admin

# Register your models here.
from cliente.modulos.landingpage.ListaProfissional import ListaProfissional, ListaEmpresa
from core.models.base.area_atendimento import AreaAtendimento
from core.models.base.endereco import Endereco
from core.models.base.lat_lng import LatLng
from core.modulos.atendente.atendente import Atendente
from core.modulos.atendimento.atendimento import Atendimento
from core.modulos.atendimentos_departamento.atendimentos_departamento import AtendimentosDepartamento
from core.modulos.cliente.cliente import Cliente
from core.modulos.departamento.departamento import Departamento
from core.modulos.empresa.empresa import Empresa
from core.modulos.escala.escala import Escala, EscalaIntervalo
from core.modulos.gerente.gerente import Gerente
from core.modulos.paciente.paciente import Paciente, PacienteDepartamentoProfissional
from core.modulos.profissional.profissional import Profissional, DepartamentoProfissional
from core.modulos.prontuario.prontuario import Prontuario
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento
from core.modulos.tipo_profissional.tipo_profissional import TipoProfissional

# BASE
from core.modulos.user_profile.user_profile import UserProfile, UserComum

admin.site.register(ListaEmpresa)
admin.site.register(ListaProfissional)
admin.site.register(AreaAtendimento)
admin.site.register(LatLng)
admin.site.register(Empresa)
admin.site.register(UserProfile)
admin.site.register(UserComum)
admin.site.register(Profissional)
admin.site.register(Departamento)
admin.site.register(Atendente)
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Gerente)
admin.site.register(AtendimentosDepartamento)
admin.site.register(Paciente)
admin.site.register(PacienteDepartamentoProfissional)
admin.site.register(TipoAtendimento)
admin.site.register(TipoProfissional)
admin.site.register(DepartamentoProfissional)
admin.site.register(Escala)
admin.site.register(EscalaIntervalo)
admin.site.register(Atendimento)
admin.site.register(Prontuario)

