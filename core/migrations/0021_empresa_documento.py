# Generated by Django 3.0.5 on 2020-04-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_remove_empresa_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='documento',
            field=models.IntegerField(default=1, verbose_name='Documento'),
            preserve_default=False,
        ),
    ]
