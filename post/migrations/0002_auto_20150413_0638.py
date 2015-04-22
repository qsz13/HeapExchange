# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='flag_user',
            field=models.ManyToManyField(related_name='flag_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
