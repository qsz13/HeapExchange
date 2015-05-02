# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20150501_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='flag',
        ),
        migrations.AddField(
            model_name='activity',
            name='flag',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='activity',
            name='initiator',
            field=models.ForeignKey(related_name='activities', default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='interested',
            field=models.ManyToManyField(related_name='interested_activities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='joined',
            field=models.ManyToManyField(related_name='joined_activities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='limit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='initiator',
            field=models.ForeignKey(related_name='courses', default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='interested',
            field=models.ManyToManyField(related_name='interested_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='joined',
            field=models.ManyToManyField(related_name='joined_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='activity',
            field=models.ManyToManyField(related_name='tags', to='post.Activity'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='course',
            field=models.ManyToManyField(related_name='tags', to='post.Course'),
        ),
    ]
