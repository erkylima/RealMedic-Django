# Generated by Django 3.2.3 on 2021-05-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0015_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'CONTATO', 'verbose_name_plural': 'CONTATOS'},
        ),
        migrations.AddField(
            model_name='contact',
            name='lido',
            field=models.BooleanField(default=False),
        ),
    ]