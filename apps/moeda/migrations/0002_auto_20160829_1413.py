# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-29 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moeda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moeda',
            name='moeda_desc',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
