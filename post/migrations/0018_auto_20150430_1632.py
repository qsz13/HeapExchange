# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20150429_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='activity',
            field=models.ManyToManyField(related_name='tag', to='post.Activity'),
        ),
        migrations.AddField(
            model_name='tag',
            name='course',
            field=models.ManyToManyField(related_name='tag', to='post.Course'),
        ),
    ]
