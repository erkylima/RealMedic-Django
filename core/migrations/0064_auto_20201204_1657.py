# Generated by Django 3.0.8 on 2020-12-04 16:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_auto_20201204_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='end',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Endereco'),
        ),
    ]
