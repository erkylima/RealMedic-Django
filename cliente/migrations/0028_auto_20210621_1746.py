# Generated by Django 3.2.3 on 2021-06-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0027_auto_20210621_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaprofissional',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='listaprofissional',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
