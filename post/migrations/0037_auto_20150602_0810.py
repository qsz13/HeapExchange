# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0036_course_has_arr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrangement',
            name='content',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
