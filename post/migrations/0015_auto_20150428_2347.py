# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0014_auto_20150423_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='initiator',
            field=models.ForeignKey(related_name='initiator', default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='interested',
            field=models.ManyToManyField(related_name='interests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='joined',
            field=models.ManyToManyField(related_name='joins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='initiator',
            field=models.ForeignKey(related_name='c_initiator', default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='interested',
            field=models.ManyToManyField(related_name='c_interests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='joined',
            field=models.ManyToManyField(related_name='c_joins', to=settings.AUTH_USER_MODEL),
        ),
    ]
