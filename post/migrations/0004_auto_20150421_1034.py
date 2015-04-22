# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_auto_20150421_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='interested',
            field=models.ManyToManyField(related_name='interested', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 10, 34, 18, 673968)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 10, 34, 18, 674076)),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 10, 34, 18, 673860)),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 10, 34, 18, 673968)),
        ),
        migrations.AlterField(
            model_name='course',
            name='initialtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 10, 34, 18, 674076)),
        ),
        migrations.AlterField(
            model_name='course',
            name='joined',
            field=models.ManyToManyField(related_name='joined', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 10, 34, 18, 673860)),
        ),
    ]
