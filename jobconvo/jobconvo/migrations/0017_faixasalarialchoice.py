# Generated by Django 4.0.6 on 2022-09-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobconvo', '0016_remove_vagadeemprego_cbescolaridade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaixaSalarialChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]