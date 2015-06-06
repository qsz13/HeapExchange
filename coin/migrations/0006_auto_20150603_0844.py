# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coin', '0005_auto_20150603_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='from_user',
        ),
        migrations.AddField(
            model_name='transfer',
            name='from_user',
            field=models.ForeignKey(related_name='expense', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='to_user',
        ),
        migrations.AddField(
            model_name='transfer',
            name='to_user',
            field=models.ForeignKey(related_name='income', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
