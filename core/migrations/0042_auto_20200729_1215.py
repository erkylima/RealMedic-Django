# Generated by Django 3.0.8 on 2020-07-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_atendimento_intervalo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escala',
            name='dia',
            field=models.DateTimeField(),
        ),
    ]