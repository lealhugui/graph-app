# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_tablefield_inner_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablefield',
            name='is_primary_key',
            field=models.BooleanField(default=False),
        ),
    ]