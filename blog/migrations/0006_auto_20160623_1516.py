# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160623_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='typeCol',
            field=models.TextField(),
        ),
    ]