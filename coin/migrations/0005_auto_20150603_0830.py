# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0004_auto_20150603_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='from_user',
            field=models.ManyToManyField(related_name='expense', to=settings.AUTH_USER_MODEL),
        ),
    ]
