from django.contrib import admin

# Register your models here.
from core.models import Empresa, UserProfile
from core.modulos.departamento.departamento import Departamento
from core.modulos.profissional.profissional import Profissional

admin.site.register(Empresa)
admin.site.register(UserProfile)
admin.site.register(Profissional)
admin.site.register(Departamento)
