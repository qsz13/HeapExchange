# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0008_auto_20150423_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referral',
            field=models.ForeignKey(related_name='refered_user', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
