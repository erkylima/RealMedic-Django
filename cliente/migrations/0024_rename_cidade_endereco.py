# Generated by Django 3.2.3 on 2021-06-21 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0023_auto_20210621_1228'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cidade',
            new_name='Endereco',
        ),
    ]
