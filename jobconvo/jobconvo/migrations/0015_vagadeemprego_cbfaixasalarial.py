# Generated by Django 4.0.6 on 2022-09-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobconvo', '0014_remove_vagadeemprego_cbfaixasalarial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagadeemprego',
            name='cbFaixaSalarial',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
