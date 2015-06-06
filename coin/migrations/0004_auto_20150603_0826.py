# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coin', '0003_auto_20150603_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='from_user',
        ),
        migrations.AddField(
            model_name='transfer',
            name='from_user',
            field=models.ManyToManyField(related_name='expense', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='to_user',
        ),
        migrations.AddField(
            model_name='transfer',
            name='to_user',
            field=models.ManyToManyField(related_name='income', to=settings.AUTH_USER_MODEL),
        ),
    ]
