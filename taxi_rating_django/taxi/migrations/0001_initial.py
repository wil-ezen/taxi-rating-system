# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('score', models.IntegerField(default=-1)),
                ('date', models.DateTimeField(verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=20)),
                ('overall_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='taxi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.Taxi'),
        ),
    ]
