# Generated by Django 3.0.5 on 2020-04-09 19:46

import core.util.util_manager
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('core', '0025_auto_20200409_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaAtendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', core.util.util_manager.UpperCaseCharField(max_length=255, verbose_name='Descricao')),
            ],
            options={
                'verbose_name': 'AREA ATENDIMENTO',
                'verbose_name_plural': 'AREAS ATENDIMENTOS',
            },
        ),
        migrations.CreateModel(
            name='TipoAtendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('descricao', core.util.util_manager.UpperCaseCharField(max_length=255, verbose_name='DESCRIÇÃO')),
            ],
            options={
                'verbose_name': 'TIPO DE ATENDIMENTO',
                'verbose_name_plural': 'TIPOS DE ATENDIMENTOS',
            },
        ),
        migrations.CreateModel(
            name='TipoProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('descricao', core.util.util_manager.UpperCaseCharField(max_length=255, verbose_name='Descrição')),
                ('areaAtendimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.AreaAtendimento')),
                ('tiposAtendimentos', models.ManyToManyField(to='core.TipoAtendimento')),
            ],
            options={
                'verbose_name': 'TIPO DE PROFISSIONAL',
                'verbose_name_plural': 'TIPOS DE PROFISSIONAIS',
            },
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('nome', core.util.util_manager.UpperCaseCharField(max_length=255, verbose_name='Nome')),
                ('usuario', core.util.util_manager.UpperCaseCharField(max_length=255, unique=True, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('senha', core.util.util_manager.UpperCaseCharField(max_length=255, verbose_name='Senha')),
                ('ativo', models.BooleanField(default=True)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profissionais', to='core.Departamento')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profissionais', to='auth.Group', verbose_name='Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profissionais', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PROFISSIONAL',
                'verbose_name_plural': 'PROFISSIONAIS',
            },
        ),
        migrations.CreateModel(
            name='DepartamentoProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Departamento')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Profissional')),
                ('tiposProfissionais', models.ManyToManyField(to='core.TipoProfissional')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='areaAtendimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empresas', to='core.AreaAtendimento'),
        ),
    ]
