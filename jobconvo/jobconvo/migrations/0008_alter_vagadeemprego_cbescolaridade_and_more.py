# Generated by Django 4.0.4 on 2022-08-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobconvo', '0007_alter_vagadeemprego_cbescolaridade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagadeemprego',
            name='cbEscolaridade',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vagadeemprego',
            name='cbFaixaSalarial',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vagadeemprego',
            name='nameJob',
            field=models.CharField(max_length=255),
        ),
    ]