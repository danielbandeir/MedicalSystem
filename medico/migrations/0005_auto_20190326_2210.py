# Generated by Django 2.1.7 on 2019-03-27 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0004_auto_20190326_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='especializacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='medico.especializacao'),
        ),
    ]
