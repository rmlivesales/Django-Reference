# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0006_auto_20170108_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale_bill',
            name='total_head',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]