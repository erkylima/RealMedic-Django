# Generated by Django 3.2 on 2021-04-21 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_listaprofissional_especi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listaprofissional',
            name='especialidade',
        ),
    ]
