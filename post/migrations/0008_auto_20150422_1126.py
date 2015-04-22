# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20150421_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 11, 26, 52, 836000)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 11, 26, 52, 837000)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 11, 26, 52, 836000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 11, 26, 52, 836000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 11, 26, 52, 837000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='initiator',
            field=models.ForeignKey(related_name='initiator', default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='interested',
            field=models.ManyToManyField(related_name='interests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='joined',
            field=models.ManyToManyField(related_name='joins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 11, 26, 52, 836000)),
        ),
    ]
