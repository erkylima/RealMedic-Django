from django.contrib import admin

# Register your models here.
from cliente.models import Contact
from cliente.modulos.landingpage.ListaProfissional import ListaEmpresa, ListaProfissional


@admin.register(Contact)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "lido")

@admin.register(ListaEmpresa)
class ListaEmpresa(admin.ModelAdmin):
    list_display = ("nome","nome_slug")

@admin.register(ListaProfissional)
class ListaProfissional(admin.ModelAdmin):
    list_display = ("nome", "Especialidades")