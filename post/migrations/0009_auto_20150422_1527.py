# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20150422_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 27, 22, 310000)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 27, 22, 311000)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 27, 22, 310000)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 27, 22, 310000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 27, 22, 311000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 27, 22, 310000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
