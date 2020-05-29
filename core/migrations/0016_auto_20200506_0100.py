# Generated by Django 3.0.5 on 2020-05-06 01:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200505_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='tempo',
            field=models.TimeField(default=datetime.datetime(2020, 5, 6, 1, 0, 2, 278266)),
        ),
        migrations.AlterField(
            model_name='escalaintervalo',
            name='atendimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Atendimento'),
        ),
        migrations.AlterField(
            model_name='tipoatendimento',
            name='tempo_padrao',
            field=models.TimeField(default=datetime.datetime(2020, 5, 6, 1, 0, 2, 272319), verbose_name='Tempo Padrão'),
        ),
    ]