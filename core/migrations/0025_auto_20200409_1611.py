# Generated by Django 3.0.5 on 2020-04-09 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_atendente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atendente',
            options={'verbose_name': 'ATENDENTE', 'verbose_name_plural': 'ATENDENTES'},
        ),
        migrations.RemoveField(
            model_name='atendente',
            name='empresa',
        ),
        migrations.AddField(
            model_name='atendente',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='atendentes', to='core.Departamento'),
        ),
    ]
