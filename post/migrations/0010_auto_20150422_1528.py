# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20150422_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 28, 5, 43000)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 28, 5, 43000)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='limit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='requirement',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 28, 5, 43000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 28, 5, 43000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 28, 5, 43000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='requirement',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 28, 5, 43000)),
        ),
    ]
