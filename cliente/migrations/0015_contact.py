# Generated by Django 3.2.3 on 2021-05-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0014_listaprofissional_servicos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
