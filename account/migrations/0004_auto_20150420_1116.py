# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_intrest_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='intrest_tag',
            field=models.ManyToManyField(related_name='intrest_profile', null=True, to='post.Tag', blank=True),
        ),
    ]
