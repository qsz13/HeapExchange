# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0002_transfer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='from_user',
            field=models.ForeignKey(related_name='expense', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='to_user',
            field=models.ForeignKey(related_name='income', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
