# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-01-23 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_auto_20190123_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='like',
            name='type_like',
            field=models.IntegerField(null=True),
        ),
    ]
