from django.contrib import admin

# Register your models here.
from cliente.models import Contact
from cliente.modulos.landingpage.ListaProfissional import ListaEmpresa, ListaProfissional, Pais, Endereco


def copy_items(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


copy_items.short_description = 'Copy Items'


class CidadeAdmin(admin.ModelAdmin):
    list_display = [
        'Endereco','uf'
    ]
    list_filter = ['nome', 'uf']
    search_fields = ['nome', 'uf']
    prepopulated_fields = {"slug": ("nome","uf",)}

@admin.register(Contact)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "lido")

@admin.register(ListaEmpresa)
class ListaEmpresa(admin.ModelAdmin):
    list_display = ("nome","nome_slug")

@admin.register(ListaProfissional)
class ListaProfissional(admin.ModelAdmin):
    list_display = ("nome", "Especialidades")

admin.site.register(Pais)
admin.site.register(Endereco, CidadeAdmin)