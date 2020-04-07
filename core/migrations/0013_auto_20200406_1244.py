# Generated by Django 3.0.4 on 2020-04-06 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200406_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='senha',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='usuario',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Usuario'),
            preserve_default=False,
        ),
    ]
