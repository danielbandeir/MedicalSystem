# Generated by Django 2.1.7 on 2019-03-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_auto_20190325_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rg',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
