# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='sale_bill',
            name='buyer_address',
        ),
        migrations.AlterField(
            model_name='sale_bill',
            name='buyer_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cattle.Buyer'),
        ),
        migrations.AlterField(
            model_name='sale_bill',
            name='total_head',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
