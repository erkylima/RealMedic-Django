# Generated by Django 3.2.3 on 2021-06-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0022_listaempresa_cidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listaprofissional',
            name='listaempresa',
        ),
        migrations.AddField(
            model_name='listaprofissional',
            name='listaempresa',
            field=models.ManyToManyField(to='cliente.ListaEmpresa'),
        ),
    ]
