# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-02 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20171101_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
                ('description', models.TextField(blank=True, help_text='Short description of the status meaning. (Optional)', null=True)),
            ],
            options={
                'verbose_name_plural': 'Time Claim Status',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
                ('description', models.TextField(blank=True, help_text='Short description of the status meaning. (Optional)', null=True)),
            ],
            options={
                'verbose_name_plural': 'Project Status',
            },
        ),
        migrations.CreateModel(
            name='VariationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
                ('description', models.TextField(blank=True, help_text='Short description of the status meaning. (Optional)', null=True)),
            ],
            options={
                'verbose_name_plural': 'Variation Status',
            },
        ),
        migrations.AlterField(
            model_name='claim',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ClaimStatus'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.VariationStatus'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.ProjectStatus'),
            preserve_default=False,
        ),
    ]