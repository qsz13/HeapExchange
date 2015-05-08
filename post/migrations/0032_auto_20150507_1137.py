# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0031_auto_20150507_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='deadline',
            field=models.DateField(null=True, verbose_name='\u62a5\u540d\u622a\u81f3'),
        ),
        migrations.AddField(
            model_name='course',
            name='deadline',
            field=models.DateField(null=True, verbose_name='\u62a5\u540d\u622a\u81f3'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='limit',
            field=models.IntegerField(null=True, verbose_name='\u4eba\u6570\u9650\u5236'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5730\u70b9'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='one_time_schedule',
            field=models.OneToOneField(null=True, blank=True, to='post.OneTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='requirement',
            field=models.CharField(max_length=500, null=True, verbose_name='\u9700\u6c42'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='sequence_time_schedule',
            field=models.OneToOneField(null=True, blank=True, to='post.SequenceTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='weekly_time_schedule',
            field=models.OneToOneField(null=True, blank=True, to='post.WeeklyTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.IntegerField(null=True, verbose_name='\u4eba\u6570\u9650\u5236'),
        ),
        migrations.AlterField(
            model_name='course',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5730\u70b9'),
        ),
        migrations.AlterField(
            model_name='course',
            name='one_time_schedule',
            field=models.OneToOneField(null=True, blank=True, to='post.OneTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0, verbose_name='\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='course',
            name='requirement',
            field=models.CharField(max_length=500, null=True, verbose_name='\u9700\u6c42'),
        ),
        migrations.AlterField(
            model_name='course',
            name='sequence_time_schedule',
            field=models.OneToOneField(null=True, blank=True, to='post.SequenceTimeSchedule'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='course',
            name='weekly_time_schedule',
            field=models.OneToOneField(null=True, blank=True, to='post.WeeklyTimeSchedule'),
        ),
    ]
