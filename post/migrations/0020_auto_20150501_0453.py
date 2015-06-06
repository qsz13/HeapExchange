# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_auto_20150501_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='initiator',
            field=models.ForeignKey(related_query_name=b'course', related_name='c_initiator', default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
