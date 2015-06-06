# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0035_auto_20150520_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='has_arr',
            field=models.BooleanField(default=False),
        ),
    ]
