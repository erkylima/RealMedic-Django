# Generated by Django 3.0.5 on 2020-04-09 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_latlng'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atendimento',
            options={'verbose_name': 'ATENDIMENTO', 'verbose_name_plural': 'ATENDIMENTOS'},
        ),
        migrations.RemoveField(
            model_name='escalaintervalo',
            name='data_cadastro',
        ),
        migrations.RemoveField(
            model_name='escalaintervalo',
            name='date_modificado',
        ),
    ]
