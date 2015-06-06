# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_auto_20150507_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='time',
        ),
        migrations.RemoveField(
            model_name='course',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='course',
            name='time',
        ),
        migrations.AlterField(
            model_name='activity',
            name='one_time_schedule',
            field=models.OneToOneField(null=True, to='post.OneTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='sequence_time_schedule',
            field=models.OneToOneField(null=True, to='post.SequenceTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='weekly_time_schedule',
            field=models.OneToOneField(null=True, to='post.WeeklyTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='course',
            name='one_time_schedule',
            field=models.OneToOneField(null=True, to='post.OneTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='course',
            name='sequence_time_schedule',
            field=models.OneToOneField(null=True, to='post.SequenceTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='course',
            name='weekly_time_schedule',
            field=models.OneToOneField(null=True, to='post.WeeklyTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='onetimeschedule',
            name='date',
            field=models.DateField(verbose_name='\u6d3b\u52a8\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='onetimeschedule',
            name='end_time',
            field=models.TimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='onetimeschedule',
            name='start_time',
            field=models.TimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]
