# Generated by Django 3.0.4 on 2020-04-06 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('core', '0015_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='hasSuperAdministrador',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuarios', to='auth.Group', verbose_name='Perfil'),
        ),
    ]
