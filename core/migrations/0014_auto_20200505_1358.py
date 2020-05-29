# Generated by Django 3.0.5 on 2020-05-05 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200505_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoatendimento',
            name='valor_padrao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='tempo',
            field=models.TimeField(default=datetime.datetime(2020, 5, 5, 13, 58, 46, 444683)),
        ),
        migrations.AlterField(
            model_name='tipoatendimento',
            name='tempo_padrao',
            field=models.TimeField(default=datetime.datetime(2020, 5, 5, 13, 58, 46, 436737)),
        ),
    ]