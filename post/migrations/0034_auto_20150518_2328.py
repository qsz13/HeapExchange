# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0033_arrangement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrangement',
            name='post',
        ),
        migrations.AddField(
            model_name='arrangement',
            name='course',
            field=models.ForeignKey(related_name='arrangements', default=1, to='post.Course'),
        ),
    ]
