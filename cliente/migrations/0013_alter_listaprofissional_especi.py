# Generated by Django 3.2 on 2021-05-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_paciente_idade'),
        ('cliente', '0012_auto_20210501_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaprofissional',
            name='especi',
            field=models.ManyToManyField(related_name='espec', to='core.TipoProfissional'),
        ),
    ]
