# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-25 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_auto_20171118_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancetype',
            name='short_title',
            field=models.CharField(default='Performance G.B.', help_text='Shorter title for mobile responsive views', max_length=60),
            preserve_default=False,
        ),
    ]
