# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookingManager', '0002_auto_20170527_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='BookingManager.PostType', verbose_name='Clasificare'),
        ),
    ]
