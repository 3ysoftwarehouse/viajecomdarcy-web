# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-29 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acomodacao',
            fields=[
                ('id_acomodacao', models.AutoField(primary_key=True, serialize=False)),
                ('acomodacao_desc', models.CharField(max_length=45, unique=True)),
            ],
        ),
    ]
