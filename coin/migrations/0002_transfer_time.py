# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
