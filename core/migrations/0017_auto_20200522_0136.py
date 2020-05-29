# Generated by Django 3.0.5 on 2020-05-22 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200506_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='fim_atendimento',
            field=models.TimeField(default=datetime.datetime(2020, 5, 22, 1, 36, 14, 713708)),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='inicio_atendimento',
            field=models.TimeField(default=datetime.datetime(2020, 5, 22, 1, 36, 14, 713708)),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='tempo',
            field=models.TimeField(default=datetime.datetime(2020, 5, 22, 1, 36, 14, 713708)),
        ),
        migrations.AlterField(
            model_name='tipoatendimento',
            name='tempo_padrao',
            field=models.TimeField(default=datetime.datetime(2020, 5, 22, 1, 36, 14, 569041), verbose_name='Tempo Padrão'),
        ),
    ]
