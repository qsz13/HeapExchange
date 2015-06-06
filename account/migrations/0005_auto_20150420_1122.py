# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150413_0638'),
        ('account', '0004_auto_20150420_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='intrest_tag',
        ),
        migrations.AddField(
            model_name='profile',
            name='interest_tag',
            field=models.ManyToManyField(related_name='interest_profile', null=True, to='post.Tag', blank=True),
        ),
    ]
