# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20170606_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]