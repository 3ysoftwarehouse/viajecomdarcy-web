# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passageiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passageiro',
            name='email_responsavel',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='nome_pai',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='responsavel',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='telefone_responsavel',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
