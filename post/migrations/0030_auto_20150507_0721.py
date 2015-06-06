# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0029_auto_20150507_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onetimeschedule',
            old_name='date',
            new_name='once_date',
        ),
        migrations.RenameField(
            model_name='onetimeschedule',
            old_name='end_time',
            new_name='once_end_time',
        ),
        migrations.RenameField(
            model_name='onetimeschedule',
            old_name='start_time',
            new_name='once_start_time',
        ),
    ]
