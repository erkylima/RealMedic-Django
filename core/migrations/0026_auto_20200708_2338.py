# Generated by Django 3.0.5 on 2020-07-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20200708_0111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'verbose_name': 'PACIENTE', 'verbose_name_plural': 'PACIENTES'},
        ),
        migrations.AddField(
            model_name='tipoatendimento',
            name='publico',
            field=models.BooleanField(default=False),
        ),
    ]