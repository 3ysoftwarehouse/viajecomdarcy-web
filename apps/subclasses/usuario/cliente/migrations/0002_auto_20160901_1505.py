# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-01 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='naturalidade',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome_pai',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero_dependentes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_residencia',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
