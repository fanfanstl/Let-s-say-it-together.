# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-10 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_confess_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confess',
            name='context',
            field=models.TextField(default=''),
        ),
    ]
