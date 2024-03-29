# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20170606_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='department_id',
        ),
        migrations.AddField(
            model_name='professor',
            name='department_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.Department', to_field='name'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
