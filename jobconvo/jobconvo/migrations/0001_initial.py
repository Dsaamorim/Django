# Generated by Django 4.0.4 on 2022-08-24 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vagasDeEmprego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameJob', models.CharField(max_length=255)),
                ('cbFaixaSalarial', models.CharField(max_length=255)),
                ('cbEscolaridade', models.CharField(max_length=255)),
            ],
        ),
    ]
