# Generated by Django 3.0.5 on 2020-07-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_paciente_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='sobre',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Sobre'),
        ),
    ]
