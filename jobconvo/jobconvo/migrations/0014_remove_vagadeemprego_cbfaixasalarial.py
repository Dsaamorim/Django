# Generated by Django 4.0.6 on 2022-09-07 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobconvo', '0013_vagadeemprego_cbfaixasalarial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vagadeemprego',
            name='cbFaixaSalarial',
        ),
    ]
