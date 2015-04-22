# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_auto_20150421_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='initiator',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 11, 58, 28, 331758)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 11, 58, 28, 331839)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 11, 58, 28, 331644)),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 11, 58, 28, 331758)),
        ),
        migrations.AlterField(
            model_name='course',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 11, 58, 28, 331839)),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 11, 58, 28, 331644)),
        ),
    ]
