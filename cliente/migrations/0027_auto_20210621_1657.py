# Generated by Django 3.2.3 on 2021-06-21 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0026_auto_20210621_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listaempresa',
            name='cidade',
        ),
        migrations.AddField(
            model_name='endereco',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='enderecos', to='cliente.listaempresa'),
        ),
    ]
