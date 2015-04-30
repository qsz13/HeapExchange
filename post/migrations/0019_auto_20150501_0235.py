# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20150430_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='flag',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tag',
            name='flag',
            field=models.IntegerField(default=1),
        ),
    ]
