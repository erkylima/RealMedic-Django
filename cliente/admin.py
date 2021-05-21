from django.contrib import admin

# Register your models here.
from cliente.models import Contact


@admin.register(Contact)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "lido")