# Generated by Django 3.0.8 on 2021-04-05 12:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaAtendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descricao')),
            ],
            options={
                'verbose_name': 'AREA ATENDIMENTO',
                'verbose_name_plural': 'AREAS ATENDIMENTOS',
            },
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('retorno', models.BooleanField(default=False)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Preço')),
                ('tempo', models.TimeField(default=django.utils.timezone.now)),
                ('inicio_atendimento', models.TimeField(blank=True, null=True)),
                ('fim_atendimento', models.TimeField(blank=True, null=True)),
                ('pago', models.BooleanField(default=False)),
                ('crm_soliciante', models.CharField(blank=True, max_length=7, verbose_name='CRM Médico Solicitante')),
            ],
            options={
                'verbose_name': 'ATENDIMENTO',
                'verbose_name_plural': 'ATENDIMENTOS',
            },
        ),
        migrations.CreateModel(
            name='AtendimentosDepartamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome')),
                ('tipo_profissional', models.IntegerField()),
                ('tempo_padrao', models.TimeField(default=django.utils.timezone.now, verbose_name='Tempo Padrão')),
                ('valor_padrao', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Preço Padrão')),
                ('publico', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ATENDIMENTO DO DEPARTAMENTO',
                'verbose_name_plural': 'ATENDIMENTOS DO DEPARTAMENTO',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descricao')),
            ],
            options={
                'verbose_name': 'DEPARTAMENTO',
                'verbose_name_plural': 'DEPARTAMENTOS',
            },
        ),
        migrations.CreateModel(
            name='DepartamentoProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Departamento')),
            ],
            options={
                'verbose_name': 'PROFISSIONAL DO DEPARTAMENTO',
                'verbose_name_plural': 'PROFISSIONAIS DO DEPARTAMENTO',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('nome_razao_social', models.CharField(max_length=255, verbose_name='Nome/Razão Social')),
                ('documento', models.CharField(max_length=18, unique=True, verbose_name='Documento')),
            ],
            options={
                'verbose_name': 'EMPRESA',
                'verbose_name_plural': 'EMPRESAS',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(blank=True, max_length=255, verbose_name='Rua')),
                ('bairro', models.CharField(blank=True, max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=2, verbose_name='Estado')),
                ('numero', models.CharField(blank=True, max_length=50, verbose_name='Nº')),
            ],
            options={
                'verbose_name': 'ENDEREÇO',
                'verbose_name_plural': 'ENDEREÇOS',
            },
        ),
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('dia', models.DateField()),
                ('departamentoProfissional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.DepartamentoProfissional')),
            ],
            options={
                'verbose_name': 'ESCALA',
                'verbose_name_plural': 'ESCALAS',
            },
        ),
        migrations.CreateModel(
            name='LatLng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
            options={
                'verbose_name': 'LatLng',
                'verbose_name_plural': 'LatLngs',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('nome', models.CharField(max_length=80, verbose_name='Nome')),
                ('mae', models.CharField(blank=True, max_length=80, null=True, verbose_name='Nome da Mãe')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('data_nascimento', models.DateField(default=datetime.date.today)),
                ('cpf', models.CharField(blank=True, default='000.000.000-00', max_length=14, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, default='0.000.000', max_length=9, verbose_name='RG')),
                ('idade', models.IntegerField(blank=True, default=10, verbose_name='Idade')),
                ('telefone', models.CharField(default='(87) 912345678', max_length=40, verbose_name='Telefone')),
                ('genero', models.IntegerField(default=1, verbose_name='Genero')),
                ('sobre', models.CharField(blank=True, default='', max_length=255, verbose_name='Sobre')),
                ('cliente_app', models.CharField(blank=True, default=None, max_length=255, verbose_name='Cliente App')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Departamento')),
                ('endereco', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='core.Endereco')),
            ],
            options={
                'verbose_name': 'PACIENTE',
                'verbose_name_plural': 'PACIENTES',
            },
        ),
        migrations.CreateModel(
            name='PacienteDepartamentoProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('departamentoProfissional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.DepartamentoProfissional')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Paciente')),
            ],
            options={
                'verbose_name': 'PACIENTE DO PROFISSINAL NO DEPARTAMENTO',
                'verbose_name_plural': 'PACIENTES DO PROFISSINAL NO DEPARTAMENTO',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('usuario', models.CharField(max_length=255, unique=True, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('senha', models.CharField(max_length=255, verbose_name='Senha')),
                ('ativo', models.BooleanField(default=True)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Departamento')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuarios', to='auth.Group', verbose_name='Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='userProfile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'USUARIO GERENCIA DE CLINICA',
                'verbose_name_plural': 'USUARIOS GERENCIA DE CLINICA',
            },
        ),
        migrations.CreateModel(
            name='UserComum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('usuario', models.CharField(max_length=255, unique=True, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('senha', models.CharField(max_length=255, verbose_name='Senha')),
                ('ativo', models.BooleanField(default=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuarioComum', to='auth.Group', verbose_name='Perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='userComum', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'USUARIO INDEPENDENTE DE CLINICA',
                'verbose_name_plural': 'USUARIOS INDEPENDENTES DE CLINICA',
            },
        ),
        migrations.CreateModel(
            name='TipoProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('areaAtendimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.AreaAtendimento')),
            ],
            options={
                'verbose_name': 'TIPO DE PROFISSIONAL',
                'verbose_name_plural': 'TIPOS DE PROFISSIONAIS',
            },
        ),
        migrations.CreateModel(
            name='TipoAtendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('descricao', models.CharField(max_length=255, verbose_name='Descricao')),
                ('areaAtendimento', models.ManyToManyField(to='core.AreaAtendimento', verbose_name='Area de Atendimento')),
                ('tipo_profissional', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.TipoProfissional')),
            ],
            options={
                'verbose_name': 'TIPO DE ATENDIMENTO GERAL',
                'verbose_name_plural': 'TIPOS DE ATENDIMENTOS GERAL',
            },
        ),
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observação')),
                ('atendimento', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.Atendimento')),
                ('departamento_profissional_paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.PacienteDepartamentoProfissional')),
            ],
            options={
                'verbose_name': 'PRONTUARIO',
                'verbose_name_plural': 'PRONTUARIOS',
            },
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('codigo', models.CharField(default='', max_length=10, verbose_name='Código')),
                ('tiposAtendimentos', models.ManyToManyField(to='core.AtendimentosDepartamento', verbose_name='Tipos de Atendimento')),
                ('userComum', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profissional', to='core.UserComum')),
            ],
            options={
                'verbose_name': 'PROFISSIONAL',
                'verbose_name_plural': 'PROFISSIONAIS',
            },
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('userProfile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='gerente', to='core.UserProfile')),
            ],
            options={
                'verbose_name': 'GERENTE',
                'verbose_name_plural': 'GERENTES',
            },
        ),
        migrations.CreateModel(
            name='EscalaIntervalo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.TimeField()),
                ('fim', models.TimeField()),
                ('descricao', models.CharField(max_length=255)),
                ('cor', models.CharField(max_length=20)),
                ('atendimento', models.IntegerField(blank=True, null=True)),
                ('escala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Escala')),
            ],
        ),
        migrations.AddField(
            model_name='departamentoprofissional',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Profissional'),
        ),
        migrations.AddField(
            model_name='departamentoprofissional',
            name='tipo_profissional',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.TipoProfissional'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empresa', to='core.Empresa'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='endereco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Endereco'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('cliente_app', models.CharField(blank=True, default='', max_length=255, verbose_name='Cliente App')),
                ('userProfile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='cliente', to='core.UserProfile')),
            ],
            options={
                'verbose_name': 'CLIENTE',
                'verbose_name_plural': 'CLIENTES',
            },
        ),
        migrations.AddField(
            model_name='atendimentosdepartamento',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Departamento'),
        ),
        migrations.AddField(
            model_name='atendimentosdepartamento',
            name='tipo_atendimento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.TipoAtendimento'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='departamentoProfissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.DepartamentoProfissional'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='intervalo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='escala_intervalo', to='core.EscalaIntervalo'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Paciente'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='tipoAtendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.AtendimentosDepartamento'),
        ),
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('userProfile', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='atendente', to='core.UserProfile')),
            ],
            options={
                'verbose_name': 'ATENDENTE',
                'verbose_name_plural': 'ATENDENTES',
            },
        ),
    ]
