# Generated by Django 3.0.8 on 2020-12-04 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_auto_20201204_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='end',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='core.Endereco'),
        ),
    ]
