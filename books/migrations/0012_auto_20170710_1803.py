# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0011_auto_20170710_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='avg_rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]