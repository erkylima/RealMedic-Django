# Generated by Django 3.0.5 on 2020-06-05 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200602_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='tempo',
            field=models.TimeField(default=datetime.datetime(2020, 6, 5, 2, 37, 21, 100242)),
        ),
        migrations.AlterField(
            model_name='tipoatendimento',
            name='tempo_padrao',
            field=models.TimeField(default=datetime.datetime(2020, 6, 5, 2, 37, 21, 93261), verbose_name='Tempo Padrão'),
        ),
    ]