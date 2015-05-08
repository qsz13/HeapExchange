# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0027_auto_20150502_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SequenceTimeSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyTimeSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='schedule_type',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='schedule_type',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='interested',
            field=models.ManyToManyField(related_name='interested_activities', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='joined',
            field=models.ManyToManyField(related_name='joined_activities', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='interested',
            field=models.ManyToManyField(related_name='interested_courses', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='joined',
            field=models.ManyToManyField(related_name='joined_courses', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='one_time_schedule',
            field=models.ForeignKey(to='post.OneTimeSchedule', null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='sequence_time_schedule',
            field=models.ForeignKey(to='post.SequenceTimeSchedule', null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='weekly_time_schedule',
            field=models.ForeignKey(to='post.WeeklyTimeSchedule', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='one_time_schedule',
            field=models.ForeignKey(to='post.OneTimeSchedule', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='sequence_time_schedule',
            field=models.ForeignKey(to='post.SequenceTimeSchedule', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='weekly_time_schedule',
            field=models.ForeignKey(to='post.WeeklyTimeSchedule', null=True),
        ),
    ]
