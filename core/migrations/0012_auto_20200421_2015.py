# Generated by Django 3.0.5 on 2020-04-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200416_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='escalaintervalo',
            name='cor',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='escalaintervalo',
            name='descricao',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
