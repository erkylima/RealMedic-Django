# Generated by Django 3.0.5 on 2020-07-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_paciente_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço'),
        ),
    ]