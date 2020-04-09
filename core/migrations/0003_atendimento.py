# Generated by Django 3.0.5 on 2020-04-09 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_escala_escalaintervalo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Cliente')),
                ('departamentoProfissional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.DepartamentoProfissional')),
                ('escalaIntervalo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.EscalaIntervalo')),
                ('tipoAtendimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.TipoAtendimento')),
            ],
            options={
                'verbose_name': 'ESCALA',
                'verbose_name_plural': 'ESCALAS',
            },
        ),
    ]
