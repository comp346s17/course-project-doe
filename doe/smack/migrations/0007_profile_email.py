# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smack', '0006_auto_20170419_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
