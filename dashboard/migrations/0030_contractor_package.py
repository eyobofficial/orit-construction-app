# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-17 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_auto_20171117_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Package'),
            preserve_default=False,
        ),
    ]
