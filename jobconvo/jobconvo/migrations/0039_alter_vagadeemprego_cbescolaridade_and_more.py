# Generated by Django 4.0.6 on 2022-09-14 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobconvo', '0038_alter_vagadeemprego_cbescolaridade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagadeemprego',
            name='cbEscolaridade',
            field=models.CharField(choices=[('faixa5', 'Ensino fundamental'), ('faixa6', 'Ensino médio'), ('faixa7', 'Tecnólogo'), ('faixa8', 'Ensino Superior'), ('faixa9', 'Pós/MBA/Mestrado'), ('faixa10', 'Doutorado')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='vagadeemprego',
            name='cbFaixaSalarial',
            field=models.CharField(choices=[('faixa1', 'R$1.000'), ('faixa2', 'R$1.000 a R$2.000'), ('faixa3', 'R$2.000 a R$3.000'), ('faixa4', 'Acima de R$3.000')], max_length=25, null=True),
        ),
    ]