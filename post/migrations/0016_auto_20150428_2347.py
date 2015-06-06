# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_auto_20150428_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='initiator',
            field=models.ForeignKey(related_name='a_initiator', default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='interested',
            field=models.ManyToManyField(related_name='a_interests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='joined',
            field=models.ManyToManyField(related_name='a_joins', to=settings.AUTH_USER_MODEL),
        ),
    ]
