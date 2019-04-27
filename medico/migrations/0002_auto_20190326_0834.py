# Generated by Django 2.1.7 on 2019-03-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='celular',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='cidade',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='cpf',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='endereco',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='estado',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='rg',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medico',
            name='sangue',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='medico',
            name='telefone',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
