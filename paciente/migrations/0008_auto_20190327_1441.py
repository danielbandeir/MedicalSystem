# Generated by Django 2.1.7 on 2019-03-27 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0007_auto_20190326_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adicionaratendimento',
            name='nomeMedico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='medico.medico'),
        ),
    ]
