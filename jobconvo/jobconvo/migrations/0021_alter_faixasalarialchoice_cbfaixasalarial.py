# Generated by Django 4.0.6 on 2022-09-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobconvo', '0020_faixasalarialchoice_cbfaixasalarial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faixasalarialchoice',
            name='cbFaixaSalarial',
            field=models.CharField(choices=[('faixa1', 'R$1.000'), ('faixa2', 'R$1.000 a R$2.000'), ('faixa3', 'R$2.000 a R$3.000'), ('faixa4', 'Acima de R$3.000')], max_length=25, null=True, unique=True),
        ),
    ]