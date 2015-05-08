# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0030_auto_20150507_0721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sequencetimeschedule',
            old_name='end_date',
            new_name='sequence_end_date',
        ),
        migrations.RenameField(
            model_name='sequencetimeschedule',
            old_name='end_time',
            new_name='sequence_end_time',
        ),
        migrations.RenameField(
            model_name='sequencetimeschedule',
            old_name='start_date',
            new_name='sequence_start_date',
        ),
        migrations.RenameField(
            model_name='sequencetimeschedule',
            old_name='start_time',
            new_name='sequence_start_time',
        ),
        migrations.RenameField(
            model_name='weeklytimeschedule',
            old_name='end_date',
            new_name='weekly_end_date',
        ),
        migrations.RenameField(
            model_name='weeklytimeschedule',
            old_name='end_time',
            new_name='weekly_end_time',
        ),
        migrations.RenameField(
            model_name='weeklytimeschedule',
            old_name='start_date',
            new_name='weekly_start_date',
        ),
        migrations.RenameField(
            model_name='weeklytimeschedule',
            old_name='start_time',
            new_name='weekly_start_time',
        ),
        migrations.AddField(
            model_name='weeklytimeschedule',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeklytimeschedule',
            name='monday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeklytimeschedule',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeklytimeschedule',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeklytimeschedule',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeklytimeschedule',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weeklytimeschedule',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]
