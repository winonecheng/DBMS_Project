# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20170606_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='head_id',
            new_name='head',
        ),
    ]
