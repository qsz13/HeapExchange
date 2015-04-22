# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20150421_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='limit',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='activity',
            name='requirement',
            field=models.CharField(default=b'DEFAULT', max_length=500),
        ),
        migrations.AddField(
            model_name='course',
            name='limit',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='course',
            name='requirement',
            field=models.CharField(default=b'DEFAULT', max_length=500),
        ),
        migrations.AlterField(
            model_name='activity',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 16, 25, 52, 291148)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 16, 25, 52, 291260)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 16, 25, 52, 291047)),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 16, 25, 52, 291148)),
        ),
        migrations.AlterField(
            model_name='course',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 16, 25, 52, 291260)),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 16, 25, 52, 291047)),
        ),
    ]
