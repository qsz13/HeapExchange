# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20150420_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=b'/media/avatar/default', upload_to=b'avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interest_tag',
            field=models.ManyToManyField(related_name='interest_profile', to='post.Tag', blank=True),
        ),
    ]
