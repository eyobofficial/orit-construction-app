# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_remove_claim_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='received_letter',
            field=models.CharField(blank=True, help_text='Ref. No. for the letter containing the order received.', max_length=100, null=True, verbose_name='Ref. No. for received Order (Optional)'),
        ),
    ]