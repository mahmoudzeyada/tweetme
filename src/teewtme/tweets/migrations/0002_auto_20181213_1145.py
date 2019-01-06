# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-13 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, validators=[tweets.validators.content_not_empty]),
        ),
    ]
