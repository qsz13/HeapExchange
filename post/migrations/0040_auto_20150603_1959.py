# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0039_auto_20150603_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityimages',
            old_name='activity',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='courseimages',
            old_name='course',
            new_name='post',
        ),
    ]
