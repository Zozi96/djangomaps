# Generated by Django 3.0.12 on 2021-02-08 01:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la tienda')),
                ('geos', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Ubicación')),
            ],
        ),
    ]
