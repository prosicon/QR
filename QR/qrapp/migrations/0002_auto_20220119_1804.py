# Generated by Django 2.2.3 on 2022-01-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='descripcion_nivel',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='descripcion_nivel_puesto',
            field=models.CharField(max_length=100),
        ),
    ]
