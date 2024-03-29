# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20170606_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='teacher_id',
            new_name='teacher',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='advisor_id',
            new_name='advisor',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='take_course_id',
            new_name='take_course',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='department_name',
        ),
        migrations.AddField(
            model_name='professor',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.Department'),
        ),
        migrations.AlterField(
            model_name='department',
            name='head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dp', to='database.Professor'),
        ),
    ]
