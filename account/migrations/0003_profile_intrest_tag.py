# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150413_0638'),
        ('account', '0002_auto_20150413_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='intrest_tag',
            field=models.ManyToManyField(related_name='intrest_profile', to='post.Tag'),
        ),
    ]
