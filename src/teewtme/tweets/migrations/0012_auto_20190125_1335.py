# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-01-25 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0011_auto_20190127_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
